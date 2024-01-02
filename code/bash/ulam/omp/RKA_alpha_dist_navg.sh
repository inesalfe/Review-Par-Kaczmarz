#!/bin/bash

# bash bash/omp/RKA_alpha_dist_navg.sh > outputs/progress/RKA_alpha_dist_navg.txt &

N=(50 100 200 500 750 1000 2000 4000 10000)
M=(2000 4000 20000 40000 80000 160000)
T=(1 2 4 8 10 12)

echo "--- Remove Old Files ---"

rm outputs/omp/RKA_alpha_dist_it.txt

echo "--- Dense RK ---"

line=1
for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then	
			for t in ${T[@]}; do
				export OMP_NUM_THREADS=1
				str="$(sed "${line}q;d" outputs/omp/RKA_best_alpha_navg.txt)"
				IFS=' ' read -r -a arr <<< "$str"
				alpha=${arr[3]}
				str=$(./bin/RKA_error_alpha_dist.exe dense 10 1E-8 $m $n $t $alpha)
				IFS=' ' read -r -a arr <<< "$str"
				it=${arr[3]}
				./bin/RKA_max_it_alpha_dist.exe dense 10 $m $n $t $alpha $it >> outputs/omp/RKA_alpha_dist_it.txt
				echo "seq $m $n $t $alpha $it"
				((line++))
			done
		fi
	done
done