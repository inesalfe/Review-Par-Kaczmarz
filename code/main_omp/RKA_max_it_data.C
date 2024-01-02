#include "aux_func.h"
#include <iostream>
#include <iomanip>
#include <math.h>
#include <omp.h>
#include <random>
#include <fstream>
#include <sstream>
using namespace std;

int main (int argc, char *argv[]) {

	if(argc != 8) {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/RKA_max_it_data.exe <data_set> <n_runs> <M> <N> <it_per_thread> <max_it_stop> <step_save>'" << endl;
		exit(1);
	}

	double* b;
	double* x;
	double* x_sol;
	double** A;

	int n_runs = atoi(argv[2]);

	int M = atoi(argv[3]);
	int N = atoi(argv[4]);
	int it_per_thread = atoi(argv[5]);
	long long max_it_stop = atoll(argv[6]);
	int step_save = atoi(argv[7]);

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
	else if (matrix_type.compare("dense_ls") == 0) {
		filename_A = "../data/dense_ls/A_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_b = "../data/dense_ls/b_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_x = "../data/dense_ls/x_" + to_string(M) + "_" + to_string(N) + ".bin";
	}
	else {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/RKA_max_it_data.exe <data_set> <n_runs> <M> <N> <it_per_thread> <max_it_stop> <step_save>'" << endl;
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

	discrete_distribution<> dist(sqrNorm_line.begin(), sqrNorm_line.end());
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

	vector<double> error;
	vector<double> res;
	vector<int> error_it;
	vector<int> res_it;
	double* res_vec = new double[M];
	double sqr_norm_res;

	for(int run = 0; run < n_runs; run++) {
		for (int i = 0; i < N; i++) {
			x_k[i] = 0;
		}
		it = 0;
        gen.clear();
        for (int i = 0; i < it_per_thread; i++) {
            gen[i] = mt19937(run*it_per_thread+i+1);
        }
		start = omp_get_wtime();
		while(it < max_it_stop) {
			it++;
			for (int i = 0; i < N; i++) {
				x_prev[i] = x_k[i];
			}
			for (int i = 0; i < it_per_thread; i++) {
				line = dist(gen[i]);
				scale = (b[line]-dotProduct(A[line], x_prev, N))/sqrNorm_line[line];
				for (int j = 0; j < N; j++) {
					x_k[j] += (scale * A[line][j])/it_per_thread;
				}
			}
			if (it%step_save == 0) {
				error_it.push_back(it);
				error.push_back(sqrt(sqrNormDiff(x_k, x, N)));
				for (int i = 0; i < M; i++) {
					res_vec[i] = b[i] - dotProduct(A[i], x_k, N);
				}
				sqr_norm_res = 0;
				for (int i = 0; i < M; i++)
					sqr_norm_res += res_vec[i]*res_vec[i];
				res_it.push_back(it);
				res.push_back(sqrt(sqr_norm_res));
			}
		}
		stop = omp_get_wtime();
		duration += stop - start;
		for (int i = 0; i < N; i++) {
			x_sol[i] += x_k[i];
		}
	}
	cout << M << " " << N << " " << duration << " " << max_it_stop << " ";

	for (int i = 0; i < N; i++) {
		x_sol[i] /= n_runs;
	}

	for (int i = 0; i < M; i++)
		res_vec[i] = b[i] - dotProduct(A[i], x_sol, N);
	cout << sqrNorm(res_vec, M) << " ";
	delete[] res_vec;

	double stop_total = omp_get_wtime();
	double duration_total = stop_total - start_total;

	cout << sqrNormDiff(x_sol, x, N) << " " << duration_total << endl;

	string filename_error = "errors/omp/RKA_error_" + to_string(M) + "_" + to_string(N) + "_" + to_string(it_per_thread) + ".txt";
	string filename_res = "errors/omp/RKA_res_" + to_string(M) + "_" + to_string(N) + "_" + to_string(it_per_thread) + ".txt";

	ofstream file_error(filename_error);
	ofstream file_res(filename_res);
	if (file_error.is_open() && file_res.is_open()) {
		for (int i = 0; i < error.size(); i++) {
			file_error << error_it[i] << " " << error[i] << endl;
			file_res << res_it[i] << " " << res[i] << endl;
		}
		file_error.close();
		file_res.close();
	}
	else {
		cout << "ERROR: Invalid input file for error or residual output file." << endl;
		exit(1);
	}

	delete[] x_k;
	delete[] x_prev;

	delete[] A[0];
	delete[] A;
	delete[] b;
	delete[] x;
	delete[] x_sol;

	return 0;
}