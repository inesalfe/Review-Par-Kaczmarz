#!/bin/bash

# bash bash/omp/RKA_best_alpha_ulam.sh > outputs/progress/RKA_best_alpha_ulam.txt &

N=(50 100 200 500 750 1000 2000 4000 10000)
M=(2000 4000 20000 40000 80000 160000)

echo "--- Remove Old Files ---"

rm outputs/omp/RKA_best_alpha_ulam.txt

echo "--- Dense RKA ---"

export OMP_NUM_THREADS=1

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then
			./bin/best_alpha_ulam.exe dense $m $n >> outputs/omp/RKA_best_alpha_ulam.txt
		fi
	done
done