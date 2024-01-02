#include "aux_func.h"
#include <iostream>
#include <math.h>
#include <mpi.h>
#include <random>
#include <fstream>
#include <sstream>
using namespace std;

#define BLOCK_LOW(id, p, np) ((id) * (np) / (p))
#define BLOCK_HIGH(id, p, np) (BLOCK_LOW((id) + 1, p, np) - 1)
#define BLOCK_SIZE(id, p, np) (BLOCK_HIGH(id, p, np) - BLOCK_LOW(id, p, np) + 1)

int nproc;

int M;
int N;

double* b;
double* x;
double* x_sol;
double** A;
double* x_k;
double* x_prev;

int n_runs;
double eps;
double alpha;

double start_total;
double stop_total;
double duration_total;
double start; 
double stop;
double duration;

vector<double> sqrNorm_line;
discrete_distribution<> dist;

double scale;
int line;
long long it;
long long avg_it;
bool solution_found;

void importMPIDenseSystemBIN(int M, int N, string A_filename, string b_filename, string x_filename, double**& A, double*& b, double*& x) {

	ifstream file_A;
	file_A.open(A_filename, ios::binary);
	if (!file_A.is_open()) {
		cout << "Error in opening the matrix file" << endl;
		exit(1);
	}

	double * aux = new double[(long)M*(long)N];
	A = new double*[(long)M];
	for (long i = 0; i < M; i++)
		A[i] = &aux[i * N];

	double temp;
	for (long i = 0; i < M; i++) {
		for (long j = 0; j < N; j++) 
			file_A.read(reinterpret_cast<char *>(&A[i][j]), sizeof(A[i][j]));
	}

	file_A.close();

	ifstream file_b;
	file_b.open(b_filename, ios::binary);
	if (!file_b.is_open()) {
		cout << "Error in opening the b vector file" << endl;
		delete[] A[0];
		delete[] A;
		exit(1);
	}

	b = new double[M];

	for (long i = 0; i < M; i++) {
		file_b.read(reinterpret_cast<char *>(&b[i]), sizeof(b[i]));
	}

	file_b.close();

	ifstream file_x;
	file_x.open(x_filename, ios::binary);
	if (!file_x.is_open()) {
		cout << "Error in opening the x vector file" << endl;
		delete[] A[0];
		delete[] A;
		delete[] b;
		exit(1);
	}

	x = new double[N];

	for (long i = 0; i < N; i++)
		file_x.read(reinterpret_cast<char *>(&x[i]), sizeof(x[i]));

	file_x.close();
}

int main (int argc, char *argv[]) {

	if(argc != 8) {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'mpirun -np <nproc> ./bin/RKA_mpi_alpha_dist.exe <data_set> <n_runs> <eps> <M> <N> <nproc> <alpha>'" << endl;
		exit(1);
	}

	MPI_Init(&argc, &argv);
	
	start_total = MPI_Wtime();

	n_runs = atoi(argv[2]);
	eps = atof(argv[3]);

	M = atoi(argv[4]);
	N = atoi(argv[5]);
	nproc = atoi(argv[6]);
	alpha = atof(argv[7]);

	string matrix_type = argv[1];
	string filename_A;
	string filename_b;
	string filename_x;
	if (matrix_type.compare("dense") == 0) {
		filename_A = "../data/dense/A_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_b = "../data/dense/b_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_x = "../data/dense/x_" + to_string(M) + "_" + to_string(N) + ".bin";
		importMPIDenseSystemBIN(M, N, filename_A, filename_b, filename_x, A, b, x);
	}
	else if (matrix_type.compare("dense_norm") == 0) {
		filename_A = "../data/dense_norm/A_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_b = "../data/dense_norm/b_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_x = "../data/dense_norm/x_" + to_string(M) + "_" + to_string(N) + ".bin";
		importMPIDenseSystemBIN(M, N, filename_A, filename_b, filename_x, A, b, x);
	}
	else if (matrix_type.compare("ls_dense") == 0) {
		filename_A = "../data/ls_dense/A_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_b = "../data/ls_dense/b_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_x = "../data/ls_dense/x_" + to_string(M) + "_" + to_string(N) + ".bin";
		importMPIDenseSystemBIN(M, N, filename_A, filename_b, filename_x, A, b, x);
	}
	else {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'mpirun -np <nproc> ./bin/RKA_mpi_alpha_dist.exe <data_set> <n_runs> <eps> <M> <N> <nproc> <alpha>'" << endl;
		exit(1);
	}	

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

	vector<discrete_distribution<>> dist(nproc);
	for (int i = 0; i < nproc; i++) {
		dist[i] = discrete_distribution<>(sqrNorm_line.begin()+BLOCK_LOW(i, nproc, M), sqrNorm_line.begin()+BLOCK_HIGH(i, nproc, M)+1);
	}
	vector<mt19937> gen(nproc);

	x_k = new double[N];
	x_prev = new double[N];
	x_sol = new double[N];
	for (int i = 0; i < N; i++) {
		x_sol[i] = 0;
	}
	duration = 0;
	avg_it = 0;

	for(int run = 0; run < n_runs; run++) {
		gen.clear();
		for (int i = 0; i < nproc; i++) {
			gen[i] = mt19937(run*nproc+i+1);
		}
		solution_found = false;
		it = 0;
		start = MPI_Wtime();
		for (int i = 0; i < N; i++) {
			x_k[i] = 0;
		}
		while(!solution_found) {
			it++;
			for (int i = 0; i < N; i++) {
				x_prev[i] = x_k[i];
			}
			for (int i = 0; i < nproc; i++) {
				line = BLOCK_LOW(i, nproc, M)+dist[i](gen[i]);
				scale = alpha * (b[line]-dotProduct(A[line], x_prev, N))/sqrNorm_line[line];
				for (int j = 0; j < N; j++) {
					x_k[j] += (scale * A[line][j])/nproc;
				}
			}
			if (sqrNormDiff(x_k, x, N) < eps)
				solution_found = true;
		}
		stop = MPI_Wtime();
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

	stop_total = MPI_Wtime();
	duration_total = stop_total - start_total;

	cout << sqrNormDiff(x_sol, x, N) << " " << duration_total << endl;

	delete[] x_k;
	delete[] x_prev;

	delete[] A[0];
	delete[] A;
	delete[] b;
	delete[] x;
	delete[] x_sol;

	MPI_Finalize();

}