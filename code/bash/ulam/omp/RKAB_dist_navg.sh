#!/bin/bash

# bash bash/omp/RKAB_dist_navg.sh >> outputs/progress/RKAB_dist_navg.txt &

N=(1000 4000 10000)
M=(4000 20000 40000 80000 160000)
K=(5 10 100 500 1000 2000 4000 10000)
T=(1 2 4 8 10 12)

echo "--- Remove Old Files ---"

rm outputs/omp/RKAB_dist_it.txt

echo "--- Dense RKAB ---"

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then
			for k in ${K[@]}; do
				for t in ${T[@]}; do
					export OMP_NUM_THREADS=1
					str=$(./bin/RKAB_error_dist.exe dense 10 1E-8 $m $n $t $k)
					IFS=' ' read -r -a arr <<< "$str"
					it=${arr[3]}
					./bin/RKAB_max_it_dist.exe dense 10 $m $n $t $k $it >> outputs/omp/RKAB_dist_it.txt
					echo "seq $m $n $t $k $it"
				done
			done
		fi
	done
done