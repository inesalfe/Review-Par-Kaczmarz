#!/bin/bash

# bash bash/mpi/RKA_alpha_dist_navg_mpi.sh > outputs/progress/RKA_alpha_dist_navg_mpi.txt &

N=(50 100 200 500 750 1000 2000 4000 10000)
M=(2000 4000 20000 40000 80000 160000)
T=(24 48)

echo "--- Remove Old Files ---"

rm outputs/mpi/RKA_alpha_dist_it_mpi.txt

echo "--- Dense RK ---"

line1=1
line2=1
for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then
			export OMP_NUM_THREADS=1
			for (( i=0; i<4; i++ )) do
				str="$(sed "${line1}q;d" outputs/omp/RKA_alpha_dist_it.txt)"
				echo "$str" >> outputs/mpi/RKA_alpha_dist_it_mpi.txt
				((line1++))
				((line2++))
			done
			((line1++))
			((line2++))
			str="$(sed "${line1}q;d" outputs/omp/RKA_alpha_dist_it.txt)"
			echo "$str" >> outputs/mpi/RKA_alpha_dist_it_mpi.txt
			((line1++))
			# ((line2++))
			for t in ${T[@]}; do
				str="$(sed "${line2}q;d" outputs/mpi/RKA_best_alpha_navg.txt)"
				IFS=' ' read -r -a arr <<< "$str"
				alpha=${arr[3]}
				str=$(./bin/RKA_error_alpha_dist.exe dense 10 1E-8 $m $n $t $alpha)
				IFS=' ' read -r -a arr <<< "$str"
				it=${arr[3]}
				./bin/RKA_max_it_alpha_dist.exe dense 10 $m $n $t $alpha $it >> outputs/mpi/RKA_alpha_dist_it_mpi.txt
				((line2++))
			done
		fi
	done
done