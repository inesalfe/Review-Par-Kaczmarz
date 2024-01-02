#include "aux_func.h"
#include <iostream>
#include <math.h>
#include <omp.h>
#include <random>
#include <fstream>
#include <sstream>
using namespace std;

#define BLOCK_LOW(id, p, np) ((id) * (np) / (p))
#define BLOCK_HIGH(id, p, np) (BLOCK_LOW((id) + 1, p, np) - 1)
#define BLOCK_SIZE(id, p, np) (BLOCK_HIGH(id, p, np) - BLOCK_LOW(id, p, np) + 1)

void importAlpha(int M, int N, int num_threads, double*& alpha) {

	alpha = new double[num_threads];

	ifstream file_alpha;
	file_alpha.open("outputs/omp/RKA_best_alpha_threads_dist.txt");
	if (!file_alpha.is_open()) {
		cout << "Error in opening the alpha values file" << endl;
		exit(1);
	}

	string line;
	string target_line = to_string(M) + " " + to_string(N) + " " + to_string(num_threads);
	while (getline(file_alpha, line)) {
		if (line.compare(target_line) == 0) {
			getline(file_alpha, line);
			goto found_line;
		}
	}

	cout << "Error: could not find alpha values in file" << endl;
	exit(1);	

	found_line:

	stringstream ss(line);
	for (int i = 0; i < num_threads; i++) {
		ss >> alpha[i];
	}

	file_alpha.close();
}

int main (int argc, char *argv[]) {

	if(argc != 7) {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/RKA_error_alphas_dist.exe <data_set> <n_runs> <eps> <M> <N> <it_per_thread>'" << endl;
		exit(1);
	}

	double* b;
	double* x;
	double* x_sol;
	double* alpha;
	double** A;

	int n_runs = atoi(argv[2]);
	double eps = atof(argv[3]);

	int M = atoi(argv[4]);
	int N = atoi(argv[5]);
	int it_per_thread = atoi(argv[6]);

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
		cout << "'./bin/RKA_error_alphas_dist.exe <data_set> <n_runs> <eps> <M> <N> <it_per_thread>'" << endl;
		exit(1);
	}

	double start_total = omp_get_wtime();

	importDenseSystemBIN(M, N, filename_A, filename_b, filename_x, A, b, x);
	importAlpha(M, N, it_per_thread, alpha);

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

	vector<discrete_distribution<>> dist(it_per_thread);
	for (int i = 0; i < it_per_thread; i++) {
		dist[i] = discrete_distribution<>(sqrNorm_line.begin()+BLOCK_LOW(i, it_per_thread, M), sqrNorm_line.begin()+BLOCK_HIGH(i, it_per_thread, M)+1);
	}
	vector<mt19937> gen(it_per_thread);

	double* x_k = new double[N];
	double* x_prev = new double[N];
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

	bool solution_found;

	for(int run = 0; run < n_runs; run++) {
		for (int i = 0; i < N; i++) {
			x_k[i] = 0;
		}
		it = 0;
		solution_found = false;
        gen.clear();
        for (int i = 0; i < it_per_thread; i++) {
            gen[i] = mt19937(run*it_per_thread+i+1);
        }
		start = omp_get_wtime();
		while(!solution_found) {
			it++;
			for (int i = 0; i < N; i++) {
				x_prev[i] = x_k[i];
			}
			for (int i = 0; i < it_per_thread; i++) {
				line = BLOCK_LOW(i, it_per_thread, M)+dist[i](gen[i]);
				scale = alpha[i] * (b[line]-dotProduct(A[line], x_prev, N))/sqrNorm_line[line];
				for (int j = 0; j < N; j++) {
					x_k[j] += (scale * A[line][j])/it_per_thread;
				}
			}
			if (sqrNormDiff(x_k, x, N) < eps)
				solution_found = true;
		}	
		stop = omp_get_wtime();
		duration += stop - start;
		for (int i = 0; i < N; i++) {
			x_sol[i] += x_k[i];
		}
		avg_it += it;
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
	delete[] x_prev;

	delete[] A[0];
	delete[] A;
	delete[] b;
	delete[] x;
	delete[] x_sol;
	delete[] alpha;

	return 0;
}