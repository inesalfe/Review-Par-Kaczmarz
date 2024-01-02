#!/bin/bash

# bash bash/omp/RKA_best_alpha_time.sh > outputs/progress/RKA_best_alpha_time.txt &

N=(10000)
M=(80000)
T=(1 2 4 8 16 64)

echo "--- Dense RKA ---"

export OMP_NUM_THREADS=1

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then
			for t in ${T[@]}; do
				START=$(date +%s.%N)
				./bin/best_alpha.exe dense $m $n $t
				END=$(date +%s.%N)
				DIFF=$(echo "$END - $START" | bc)
				echo "$m $n $t $DIFF"
			done
		fi
	done
done