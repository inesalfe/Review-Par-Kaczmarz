#include "aux_func.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <Eigen/Dense>

#define BLOCK_LOW(id, p, np) ((id) * (np) / (p))
#define BLOCK_HIGH(id, p, np) (BLOCK_LOW((id) + 1, p, np) - 1)
#define BLOCK_SIZE(id, p, np) (BLOCK_HIGH(id, p, np) - BLOCK_LOW(id, p, np) + 1)

using Eigen::FullPivLU;
using Eigen::BDCSVD;
using Eigen::MatrixXd;
using Eigen::VectorXd;
using namespace std;

int main(int argc, char *argv[]) {

	if(argc != 4) {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/best_alpha_ulam_dist.exe <data_set> <M> <N>'" << endl;
		exit(1);
	}

	int M;
	int N;
	double** A_matrix;
	double* b_vector;
	double* x_vector;

	M = atoi(argv[2]);
	N = atoi(argv[3]);

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
		cout << "'./bin/best_alpha_ulam_dist.exe <data_set> <M> <N>'" << endl;
		exit(1);
	}

	MatrixXd m(M,N);
		for (int i = 0; i < M; i++)
			for (int j = 0; j < N; j++)
				m(i,j) = A_matrix[i][j];

	delete[] A_matrix[0];
	delete[] A_matrix;
	delete[] b_vector;
	delete[] x_vector;

    vector<int> q_values{1, 2, 4, 8, 16, 64};

	for (int q_idx = 0; q_idx < q_values.size(); q_idx++) {

		int q = q_values[q_idx];

		cout << M << " " << N << " " << q << endl;

		if (q == 1) {

			cout << 1 << " ";

		}
		else {

			for (int id = 0; id < q; id++) {

				int M_block = BLOCK_SIZE(id, q, M);

				MatrixXd m_block(M_block,N);
				for (int i = BLOCK_LOW(id, q, M); i <= BLOCK_HIGH(id, q, M); i++)
					for (int j = 0; j < N; j++)
						m_block(i-BLOCK_LOW(id, q, M),j) = m(i,j);

				BDCSVD<MatrixXd> svd(m_block);
				auto sigma = svd.singularValues();
				auto min_sing_val = sigma(sigma.size()-1);
				auto max_sing_val = sigma(0);
				auto norm = m_block.norm();

				double s_min = (min_sing_val/norm)*(min_sing_val/norm);
				double s_max = (max_sing_val/norm)*(max_sing_val/norm);

				double best_alpha;
				double threads = (double)q;
				if ((s_max-s_min) <= (1/(threads-1))) {
					best_alpha = threads/(1+(threads-1)*s_min);
				}
				else {
					best_alpha = 2*threads/(1+(threads-1)*(s_min+s_max));
				}

				cout << best_alpha << " ";

			}

		}

		cout << endl;

	}

	return 0;

}