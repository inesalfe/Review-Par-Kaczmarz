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
		cout << "'./bin/RKAB_parallel_error_dist.exe <data_set> <n_runs> <eps> <M> <N> <block_size>" << endl;
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
		cout << "'./bin/RKAB_parallel_error_dist.exe <data_set> <n_runs> <eps> <M> <N> <block_size>" << endl;
		exit(1);
	}

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

	int t_id;
	bool solution_found;
	double norm_dif;
	double dif;
	int num_threads;
	long long it_final;

	#pragma omp parallel
	{
		#pragma omp single
			num_threads = omp_get_num_threads();
	}

	for(int run = 0; run < n_runs; run++) {
		for (int i = 0; i < N; i++) {
			x_k[i] = 0;
		}
		it = 0;
		solution_found = false;
		start = omp_get_wtime();
		#pragma omp parallel private(line, scale, t_id, x_k_thread) firstprivate(it)
		{
			x_k_thread = new double[N];
			t_id = omp_get_thread_num();
			mt19937 generator(run*num_threads+t_id+1);
			discrete_distribution<> dist(sqrNorm_line.begin()+BLOCK_LOW(t_id, num_threads, M), sqrNorm_line.begin()+BLOCK_LOW(t_id, num_threads, M)+BLOCK_SIZE(t_id, num_threads, M));
			while(!solution_found) {
				it++;
				#pragma omp barrier
				line = BLOCK_LOW(t_id, num_threads, M)+dist(generator);
				scale = (b[line]-dotProduct(A[line], x_k, N))/sqrNorm_line[line];
				for (int j = 0; j < N; j++) {
					x_k_thread[j] = x_k[j] + scale * A[line][j];
				}
				for (int i = 0; i < block_size-1; i++) {
					line = BLOCK_LOW(t_id, num_threads, M)+dist(generator);
					scale = (b[line]-dotProduct(A[line], x_k_thread, N))/sqrNorm_line[line];
					for (int j = 0; j < N; j++) {
						x_k_thread[j] += scale * A[line][j];
					}
				}
				for (int i = 0; i < N; i++) {
					x_k_thread[i] -= x_k[i];
				}
				#pragma omp barrier
				#pragma omp critical
					for (int i = 0; i < N; i++)
						x_k[i] += x_k_thread[i]/num_threads;
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
