#include "aux_func.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <Eigen/Dense>

using Eigen::FullPivLU;
using Eigen::BDCSVD;
using Eigen::MatrixXd;
using Eigen::VectorXd;
using namespace std;

int main(int argc, char *argv[]) {

	if(argc != 5) {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/best_alpha.exe <data_set> <M> <N> <threads>'" << endl;
		exit(1);
	}

	int M;
	int N;
	double** A_matrix;
	double* b_vector;
	double* x_vector;

	M = atoi(argv[2]);
	N = atoi(argv[3]);
	double threads = atof(argv[4]);

	string matrix_type = argv[1];
	string filename_A;
	string filename_b;
	string filename_x;
	if (matrix_type.compare("dense") == 0) {
		filename_A = "../data/dense/A_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_b = "../data/dense/b_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_x = "../data/dense/x_" + to_string(M) + "_" + to_string(N) + ".bin";
		importDenseSystemBIN(M, N, filename_A, filename_b, filename_x, A_matrix, b_vector, x_vector);
	}
	else {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/best_alpha.exe <data_set> <M> <N> <threads>'" << endl;
		exit(1);
	}

	int q = (int)threads;

	if (q == 1) {
		cout << M << " " << N << " " << 1 << " " << 1 << endl;
		return 0;
	}

	MatrixXd m(M,N);
		for (int i = 0; i < M; i++)
			for (int j = 0; j < N; j++)
				m(i,j) = A_matrix[i][j];

	delete[] A_matrix[0];
	delete[] A_matrix;
	delete[] b_vector;
	delete[] x_vector;

	BDCSVD<MatrixXd> svd(m);
    auto sigma = svd.singularValues();
    auto min_sing_val = sigma(sigma.size()-1);
    auto max_sing_val = sigma(0);
    auto norm = m.norm();

    double s_min = (min_sing_val/norm)*(min_sing_val/norm);
    double s_max = (max_sing_val/norm)*(max_sing_val/norm);

    double best_alpha;
	if ((s_max-s_min) <= (1/(threads-1))) {
		best_alpha = threads/(1+(threads-1)*s_min);
	}
	else {
		best_alpha = 2*threads/(1+(threads-1)*(s_min+s_max));
	}
	cout << M << " " << N << " " << threads << " " << best_alpha << endl;

	return 0;

}