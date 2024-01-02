#!/bin/bash

# bash bash/omp/RKA_alphas_dist_16.sh > outputs/progress/RKA_alphas_dist_16.txt &

N=(50 100 200 500 750 1000 2000 4000 10000)
M=(2000 4000 20000 40000 80000 160000)
T=(1 2 4 8 16)

echo "--- Remove Old Files ---"

rm outputs/omp/RKA_alphas_dist_16.txt

echo "--- Dense RK ---"

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then	
			for t in ${T[@]}; do
				export OMP_NUM_THREADS=1
				./bin/RKA_error_alphas_dist.exe dense 10 1E-8 $m $n $t >> outputs/omp/RKA_alphas_dist_16.txt
			done
		fi
	done
done