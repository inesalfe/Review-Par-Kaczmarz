#!/bin/bash

# bash bash/omp/RK.sh > outputs/progress/RK.txt &

N=(50 100 200 500 750 1000 2000 4000 10000 20000)
M=(2000 4000 20000 40000 80000 160000)
T=(1 2 4 8 16 64)

echo "--- Remove Old Files ---"

rm outputs/omp/RK.txt

echo "--- Dense RK ---"

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then
			export OMP_NUM_THREADS=1
			str=$(./bin/RK_error.exe dense 10 1E-8 $m $n)
			IFS=' ' read -r -a arr <<< "$str"
			it=${arr[3]}
			./bin/RK_max_it.exe dense 10 $m $n $it >> outputs/omp/RK.txt
			echo "seq $m $n $it"
		fi
	done
done