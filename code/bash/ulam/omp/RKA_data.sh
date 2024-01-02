#!/bin/bash

# bash bash/omp/RKA_data.sh > outputs/progress/RKA_data.txt &

export OMP_NUM_THREADS=1

./bin/RKA_max_it_alpha_data.exe dense_ls 1 80000 1000 1 1 30000 100
echo "80000 1000 1 1 30000 100"
./bin/RKA_max_it_alpha_data.exe dense_ls 1 80000 1000 2 1.99864 30000 100
echo "80000 1000 2 1.99864 30000 100"
./bin/RKA_max_it_alpha_data.exe dense_ls 1 80000 1000 4 3.99183 30000 100
echo "80000 1000 4 3.99183 30000 100"
./bin/RKA_max_it_alpha_data.exe dense_ls 1 80000 1000 8 7.96199 30000 100
echo "80000 1000 8 7.96199 30000 100"
./bin/RKA_max_it_alpha_data.exe dense_ls 1 80000 1000 20 17.6373 30000 100
echo "80000 1000 20 17.6373 30000 100"
./bin/RKA_max_it_alpha_data.exe dense_ls 1 80000 1000 50 23.4198 30000 100
echo "80000 1000 50 23.4198 30000 100"

./bin/RKA_max_it_data.exe dense_ls 1 80000 1000 1 30000 100
echo "80000 1000 1 30000 100"
./bin/RKA_max_it_data.exe dense_ls 1 80000 1000 2 30000 100
echo "80000 1000 2 30000 100"
./bin/RKA_max_it_data.exe dense_ls 1 80000 1000 4 30000 100
echo "80000 1000 4 30000 100"
./bin/RKA_max_it_data.exe dense_ls 1 80000 1000 8 30000 100
echo "80000 1000 8 30000 100"
./bin/RKA_max_it_data.exe dense_ls 1 80000 1000 20 30000 100
echo "80000 1000 20 30000 100"
./bin/RKA_max_it_data.exe dense_ls 1 80000 1000 50 30000 100
echo "80000 1000 50 30000 100"