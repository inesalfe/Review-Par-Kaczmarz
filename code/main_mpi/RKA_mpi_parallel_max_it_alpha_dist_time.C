#include "aux_func.h"
#include <iostream>
#include <math.h>
#include <mpi.h>
#include <random>
#include <fstream>
#include <sstream>
using namespace std;

// mpic++ -o bin/RKA_mpi_parallel_max_it_alpha_dist.exe main_mpi/RKA_mpi_parallel_max_it_alpha_dist.C
// mpirun -np 2 ./bin/RKA_mpi_parallel_max_it_alpha_dist.exe dense 1 1E-10 2000 100 20

#define BLOCK_LOW(id, p, np) ((id) * (np) / (p))
#define BLOCK_HIGH(id, p, np) (BLOCK_LOW((id) + 1, p, np) - 1)
#define BLOCK_SIZE(id, p, np) (BLOCK_HIGH(id, p, np) - BLOCK_LOW(id, p, np) + 1)

int np;
int id;
int M_size;
int* M_size_vector;

int M;
int N;

double* b;
double* x;
double* x_sol;
double** A;
double* x_k;

int n_runs;
long long max_it_stop;
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

double start_reduce;
double end_reduce;
double duration_reduce = 0;

void importMPIDenseSystemBIN(int M, int N, string A_filename, string b_filename, string x_filename, double**& A, double*& b, double*& x) {

	ifstream file_A;
	file_A.open(A_filename, ios::binary);
	if (!file_A.is_open()) {
		cout << "Error in opening the matrix file" << endl;
		exit(1);
	}

	double * aux = new double[(long)M_size*(long)N];
	A = new double*[(long)M_size];
	for (long i = 0; i < M_size; i++)
		A[i] = &aux[i * N];

	double temp;
	for (long i = 0; i < M; i++) {
		if (i >= BLOCK_LOW(id, np, M) && i <= BLOCK_HIGH(id, np, M))
			for (long j = 0; j < N; j++) 
				file_A.read(reinterpret_cast<char *>(&A[i-BLOCK_LOW(id, np, M)][j]), sizeof(A[i-BLOCK_LOW(id, np, M)][j]));
		else
			for (long j = 0; j < N; j++) 
				file_A.read(reinterpret_cast<char *>(&temp), sizeof(temp));
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

	b = new double[M_size];

	for (long i = 0; i < M; i++) {
		if (i >= BLOCK_LOW(id, np, M) && i <= BLOCK_HIGH(id, np, M))
			file_b.read(reinterpret_cast<char *>(&b[i-BLOCK_LOW(id, np, M)]), sizeof(b[i-BLOCK_LOW(id, np, M)]));
		else
			file_b.read(reinterpret_cast<char *>(&temp), sizeof(temp));
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

	MPI_Init(&argc, &argv);

	MPI_Barrier(MPI_COMM_WORLD);
	start_total = MPI_Wtime();

    MPI_Comm_rank(MPI_COMM_WORLD, &id);
    MPI_Comm_size(MPI_COMM_WORLD, &np);

	if(argc != 7) {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'mpirun -np <nproc> ./bin/RKA_mpi_parallel_max_it_alpha_dist_time.exe <data_set> <n_runs> <M> <N> <alpha> <max_it_stop>'" << endl;
		exit(1);
	}

	n_runs = atoi(argv[2]);

	M = atoi(argv[3]);
	N = atoi(argv[4]);
	alpha = atof(argv[5]);
	max_it_stop = atoll(argv[6]);

	M_size = BLOCK_SIZE(id, np, M);

	M_size_vector = new int[np];
	for (int i = 0; i < np; i++)
		M_size_vector[i] = 0;
	M_size_vector[id] = M_size;

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
		cout << "'mpirun -np <nproc> ./bin/RKA_mpi_parallel_max_it_alpha_dist_time.exe <data_set> <n_runs> <M> <N> <alpha> <max_it_stop>'" << endl;
		exit(1);
	}	

	sqrNorm_line = vector<double>(M_size);
	for (int i = 0; i < M_size; i++) {
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

	dist = discrete_distribution<>(sqrNorm_line.begin(), sqrNorm_line.end());

	x_k = new double[N];
	x_sol = new double[N];
	for (int i = 0; i < N; i++) {
		x_sol[i] = 0;
	}
	duration = 0;

	for(int run = 0; run < n_runs; run++) {
		mt19937 generator(run*np+id+1);
		it = 0;
		MPI_Barrier(MPI_COMM_WORLD);
		start = MPI_Wtime();
		for (int i = 0; i < N; i++) {
			x_k[i] = 0;
		}
		while(it < max_it_stop) {
			it++;
			line = dist(generator);
			scale = alpha * (b[line]-dotProduct(A[line], x_k, N))/sqrNorm_line[line];
			for (int i = 0; i < N; i++) {
				x_k[i] = (x_k[i] + scale * A[line][i])/np;
			}
			MPI_Barrier(MPI_COMM_WORLD);
			start_reduce = MPI_Wtime();
			MPI_Allreduce(MPI_IN_PLACE, x_k, N, MPI_DOUBLE, MPI_SUM, MPI_COMM_WORLD);
			end_reduce = MPI_Wtime();
			duration_reduce += end_reduce-start_reduce;
		}
		stop = MPI_Wtime();
		MPI_Barrier(MPI_COMM_WORLD);
		duration += stop - start;
		for (int i = 0; i < N; i++) {
			x_sol[i] += x_k[i];
		}
	}

	for (int i = 0; i < N; i++) {
		x_sol[i] /= n_runs;
	}
	double res_entry;
	double sqrNorm_res_partial = 0;
	double sqrNorm_res = 0;
	for (int i = 0; i < M_size; i++) {
		res_entry = b[i] - dotProduct(A[i], x_sol, N);
		sqrNorm_res_partial += res_entry*res_entry;
	}
	
	MPI_Allreduce(&sqrNorm_res_partial, &sqrNorm_res, 1, MPI_DOUBLE, MPI_SUM, MPI_COMM_WORLD);

	if (!id) {

		cout << M << " " << N << " " << duration << " " << max_it_stop << " ";

		cout << sqrNorm_res << " ";

		stop_total = MPI_Wtime();
		duration_total = stop_total - start_total;

		cout << sqrNormDiff(x_sol, x, N) << " " << duration_total << " " << duration_reduce << endl;

	}

	delete[] x_k;

	delete[] A[0];
	delete[] A;
	delete[] b;
	delete[] x;
	delete[] x_sol;

	delete[] M_size_vector;
	
	MPI_Finalize();

}