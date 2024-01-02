#!/bin/bash

# bash bash/omp/RKA.sh > outputs/progress/RKA.txt &

N=(50 100 200 500 750 1000 2000 4000 10000)
M=(2000 4000 20000 40000 80000 160000)
T=(1 2 4 8 16 64)

echo "--- Remove Old Files ---"

rm outputs/omp/RKA.txt

echo "--- Dense RK ---"

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then
			for t in ${T[@]}; do
				export OMP_NUM_THREADS=1
				str=$(./bin/RKA_error.exe dense 10 1E-8 $m $n $t)
				IFS=' ' read -r -a arr <<< "$str"
				it=${arr[3]}
				./bin/RKA_max_it.exe dense 10 $m $n $t $it >> outputs/omp/RKA.txt
				echo "seq $m $n $t $it"
				export OMP_NUM_THREADS=$t
				./bin/RKA_parallel_max_it.exe dense 10 $m $n $it >> outputs/omp/RKA.txt
				echo "par $m $n $t $it"
			done
		fi
	done
done