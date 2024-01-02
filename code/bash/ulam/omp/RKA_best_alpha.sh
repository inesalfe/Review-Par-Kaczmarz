#!/bin/bash

# bash bash/omp/RKA_best_alpha.sh > outputs/progress/RKA_best_alpha.txt &

N=(50 100 200 500 750 1000 2000 4000 10000)
M=(2000 4000 20000 40000 80000 160000)
T=(1 2 4 8 10 12)

echo "--- Remove Old Files ---"

rm outputs/omp/RKA_best_alpha_navg.txt

echo "--- Dense RKA ---"

export OMP_NUM_THREADS=1

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then
			for t in ${T[@]}; do
				./bin/best_alpha.exe dense $m $n $t >> outputs/omp/RKA_best_alpha_navg.txt
			done
		fi
	done
done