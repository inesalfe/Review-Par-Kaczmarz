#!/bin/bash

# bash bash/mpi/RKA_best_alpha_mpi.sh > outputs/progress/RKA_best_alpha_mpi.txt &

N=(50 100 200 500 750 1000 2000 4000 10000)
M=(2000 4000 20000 40000 80000 160000)
T=(24 48)

echo "--- Remove Old Files ---"

rm outputs/mpi/RKA_best_alpha_navg.txt

echo "--- Dense RKA ---"

export OMP_NUM_THREADS=1

line=1
for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then
			for (( i=0; i<4; i++ )) do
				str="$(sed "${line}q;d" outputs/omp/RKA_best_alpha_navg.txt)"
				echo "$str" >> outputs/mpi/RKA_best_alpha_navg.txt
				((line++))
			done
			((line++))
			str="$(sed "${line}q;d" outputs/omp/RKA_best_alpha_navg.txt)"
			echo "$str" >> outputs/mpi/RKA_best_alpha_navg.txt
			((line++))
			for t in ${T[@]}; do
				./bin/best_alpha.exe dense $m $n $t >> outputs/mpi/RKA_best_alpha_navg.txt
			done
		fi
	done
done