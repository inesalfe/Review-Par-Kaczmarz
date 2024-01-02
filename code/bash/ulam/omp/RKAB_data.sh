#!/bin/bash

# bash bash/omp/RKAB_data.sh > outputs/progress/RKAB_data.txt &

export OMP_NUM_THREADS=1

./bin/RKAB_max_it_data.exe dense_ls 1 80000 1000 1 1000 30 1
echo "80000 1000 1 1000 30 1"
./bin/RKAB_max_it_data.exe dense_ls 1 80000 1000 2 1000 30 1
echo "80000 1000 2 1000 30 1"
./bin/RKAB_max_it_data.exe dense_ls 1 80000 1000 4 1000 30 1
echo "80000 1000 4 1000 30 1"
./bin/RKAB_max_it_data.exe dense_ls 1 80000 1000 8 1000 30 1
echo "80000 1000 8 1000 30 1"
./bin/RKAB_max_it_data.exe dense_ls 1 80000 1000 20 1000 30 1
echo "80000 1000 20 1000 30 1"
./bin/RKAB_max_it_data.exe dense_ls 1 80000 1000 50 1000 30 1
echo "80000 1000 50 1000 30 1"