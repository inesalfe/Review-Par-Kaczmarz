#!/bin/bash

# bash bash/mpi/RKAB_dist_navg_mpi.sh > outputs/progress/RKAB_dist_navg_mpi.txt &

N=(1000 4000 10000)
M=(4000 20000 40000 80000 160000)
K=(5 10 100 500 1000 2000 4000 10000)
T=(24 48)

echo "--- Remove Old Files ---"

rm outputs/mpi/RKAB_dist_it_mpi.txt

echo "--- Dense RK ---"

line=1
for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then
			for k in ${K[@]}; do
				export OMP_NUM_THREADS=1
				for (( i=0; i<4; i++ )) do
					str="$(sed "${line}q;d" outputs/omp/RKAB_dist_it.txt)"
					echo "$str" >> outputs/mpi/RKAB_dist_it_mpi.txt
					((line++))
				done
				((line++))
				str="$(sed "${line}q;d" outputs/omp/RKAB_dist_it.txt)"
				echo "$str" >> outputs/mpi/RKAB_dist_it_mpi.txt
				((line++))
				for t in ${T[@]}; do
					str=$(./bin/RKAB_error_dist.exe dense 10 1E-8 $m $n $t $k)
					IFS=' ' read -r -a arr <<< "$str"
					it=${arr[3]}
					./bin/RKAB_max_it_dist.exe dense 10 $m $n $t $k $it >> outputs/mpi/RKAB_dist_it_mpi.txt
				done
			done
		fi
	done
done