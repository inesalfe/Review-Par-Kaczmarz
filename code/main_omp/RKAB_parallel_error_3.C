#include "aux_func.h"
#include <iostream>
#include <math.h>
#include <omp.h>
#include <random>
using namespace std;

#define BLOCK_LOW(id, p, np) ((id) * (np) / (p))
#define BLOCK_HIGH(id, p, np) (BLOCK_LOW((id) + 1, p, np) - 1)
#define BLOCK_SIZE(id, p, np) (BLOCK_HIGH(id, p, np) - BLOCK_LOW(id, p, np) + 1)

int main (int argc, char *argv[]) {

	if(argc != 7) {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/RKAB_parallel_error_3.exe <data_set> <n_runs> <eps> <M> <N> <block_size>" << endl;
		exit(1);
	}

	double* b;
	double* x;
	double* x_sol;
	double** A;

	int n_runs = atoi(argv[2]);
	double eps = atof(argv[3]);

	int M = atoi(argv[4]);
	int N = atoi(argv[5]);
	int block_size = atoi(argv[6]);

	if (block_size < 2) {
		cout << "Invalid parameter: Block size must be larger than 1." << endl;
		exit(1);
	}
	
	string matrix_type = argv[1];
	string filename_A;
	string filename_b;
	string filename_x;
	if (matrix_type.compare("dense") == 0) {
		filename_A = "../data/dense/A_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_b = "../data/dense/b_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_x = "../data/dense/x_" + to_string(M) + "_" + to_string(N) + ".bin";
	}
	else if (matrix_type.compare("dense_norm") == 0) {
		filename_A = "../data/dense_norm/A_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_b = "../data/dense_norm/b_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_x = "../data/dense_norm/x_" + to_string(M) + "_" + to_string(N) + ".bin";
	}
	else {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/RKAB_parallel_error_3.exe <data_set> <n_runs> <eps> <M> <N> <block_size>" << endl;
		exit(1);
	}

	int num_threads = omp_get_max_threads();
	if (num_threads%2 != 0) {
		cout << "Error: Number of threads must be an even number." << endl;
		exit(1);
	}
	int block_threads = num_threads/2;

	double start_total = omp_get_wtime();

	importDenseSystemBIN(M, N, filename_A, filename_b, filename_x, A, b, x);

	vector<double> sqrNorm_line(M);
	for (int i = 0; i < M; i++) {
		sqrNorm_line[i] = sqrNorm(A[i], N);
		if (sqrNorm_line[i] == 0) {
			cout << "Invalid input: matrix with zero norm line" << endl;
			delete[] A[0];
			delete[] A;
			delete[] b;
			delete[] x;
			exit(1);
		}
	}

	discrete_distribution<> dist(sqrNorm_line.begin(), sqrNorm_line.end());

	double* x_k = new double[N];
	double* x_k_thread;
	x_sol = new double[N];
	for (int i = 0; i < N; i++) {
		x_sol[i] = 0;
	}
	double scale;
	int line;
	long long it;

	double start; 
	double stop;
	double duration = 0;

	long long avg_it = 0;

	int t_id_out;
	int t_id_in;
	bool solution_found;
	double norm_dif;
	double dif;
	long long it_final;

	omp_set_nested(1);
	// omp_set_dynamic(0);
	for(int run = 0; run < n_runs; run++) {
		for (int i = 0; i < N; i++) {
			x_k[i] = 0;
		}
		it = 0;
		solution_found = false;
		start = omp_get_wtime();
		#pragma omp parallel num_threads(block_threads) private(t_id_out, x_k_thread) firstprivate(it)
		{
			x_k_thread = new double[N];
			t_id_out = omp_get_thread_num();
			vector<mt19937> generator(2);
			generator[0] = mt19937(block_threads*run*2+t_id_out*block_threads+1);
			generator[1] = mt19937(block_threads*run*2+t_id_out*block_threads+2);
			while(!solution_found) {
				it++;
				// Não é preciso a barreira de baixo por causa do single na linha 154 (tem barreira implícita)
				// #pragma omp barrier
				#pragma omp parallel num_threads(2) private(line, scale, t_id_in)
				{
					t_id_in = omp_get_thread_num();
					#pragma omp for
						for (int j = 0; j < N; j++)
							x_k_thread[j] = x_k[j];
					for (int i = 0; i < block_size; i++) {
						line = dist(generator[t_id_in]);
						scale = (b[line]-dotProduct(A[line], x_k_thread, N))/sqrNorm_line[line];
						for (int j = BLOCK_LOW(t_id_in, 2, N); j < BLOCK_LOW(t_id_in, 2, N)+BLOCK_SIZE(t_id_in, 2, N); j++)
							x_k_thread[j] += scale * A[line][j];
					}
					#pragma omp barrier
					#pragma omp for
						for (int j = 0; j < N; j++)
							x_k_thread[j] -= x_k[j];
				}
				// Não é preciso a barreira de baixo por causa do for na linha 139 (tem barreira implícita)
				// #pragma omp barrier
				#pragma omp critical
					for (int i = 0; i < N; i++)
						x_k[i] += x_k_thread[i]/block_threads;
				#pragma omp single
					norm_dif = 0;
				#pragma omp for reduction(+:norm_dif)
					for (int i = 0; i < N; i++) {
						dif = x_k[i] - x[i];
						norm_dif += dif*dif;
					}
				#pragma omp single
					if (norm_dif < eps) {
						it_final = it;
						solution_found = true;
					}
			}
			delete[] x_k_thread;
		}
		stop = omp_get_wtime();
		duration += stop - start;
		for (int i = 0; i < N; i++) {
			x_sol[i] += x_k[i];
		}
		avg_it += it_final;
	}
	avg_it /= n_runs;
	cout << M << " " << N << " " << duration << " " << avg_it << " ";

	for (int i = 0; i < N; i++) {
		x_sol[i] /= n_runs;
	}

	double* res = new double[M];
	for (int i = 0; i < M; i++)
		res[i] = b[i] - dotProduct(A[i], x_sol, N);
	cout << sqrNorm(res, M) << " ";
	delete[] res;

	double stop_total = omp_get_wtime();
	double duration_total = stop_total - start_total;

	cout << sqrNormDiff(x_sol, x, N) << " " << duration_total << endl;

	delete[] x_k;

	delete[] A[0];
	delete[] A;
	delete[] b;
	delete[] x;
	delete[] x_sol;

	return 0;
}
