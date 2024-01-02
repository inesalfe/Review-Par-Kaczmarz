#!/bin/bash

# bash bash/omp/RKAB_alpha.sh >> outputs/progress/RKAB_alpha.txt &

echo "--- Remove Old Files ---"

rm outputs/omp/RKAB_alpha.txt

echo "--- Dense RKAB Single ---"

# Tudo okey

N=(1000)
M=(80000)
K=(50 500 1000)
T=(2)
A=(1.0 1.2 1.3 1.5 1.8 1.99864)

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then
			for k in ${K[@]}; do
				for alpha in ${A[@]}; do
					export OMP_NUM_THREADS=1
					str=$(./bin/RKAB_error_alpha.exe dense 10 1E-10 $m $n 2 $k $alpha)
					IFS=' ' read -r -a arr <<< "$str"
					it=${arr[3]}
					./bin/RKAB_max_it_alpha.exe dense 10 $m $n 2 $k $alpha $it >> outputs/omp/RKAB_alpha.txt
					echo "seq $m $n 2 $k $it"
					export OMP_NUM_THREADS=2
					./bin/RKAB_parallel_max_it_alpha.exe dense 10 $m $n $k $alpha $it >> outputs/omp/RKAB_alpha.txt
					echo "par $m $n 2 $k $it"
				done
			done
		fi
	done
done

# 3.0 3.99183 não converge para K=500
# 3.0 3.99183 não converge para K=1000

N=(1000)
M=(80000)
K=(50 500 1000)
T=(4)
A=(1.0 1.5 2.0 2.5 3.0 3.99183)

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then
			for k in ${K[@]}; do
				for alpha in ${A[@]}; do
					export OMP_NUM_THREADS=1
					str=$(./bin/RKAB_error_alpha.exe dense 10 1E-10 $m $n 4 $k $alpha)
					IFS=' ' read -r -a arr <<< "$str"
					it=${arr[3]}
					./bin/RKAB_max_it_alpha.exe dense 10 $m $n 4 $k $alpha $it >> outputs/omp/RKAB_alpha.txt
					echo "seq $m $n 4 $k $it"
					export OMP_NUM_THREADS=4
					./bin/RKAB_parallel_max_it_alpha.exe dense 10 $m $n $k $alpha $it >> outputs/omp/RKAB_alpha.txt
					echo "par $m $n 4 $k $it"
				done
			done
		fi
	done
done

# Tudo okey

N=(4000)
M=(80000)
K=(500 1000 4000)
T=(2)
A=(1.0 1.2 1.3 1.5 1.8 1.99976)

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then
			for k in ${K[@]}; do
				for alpha in ${A[@]}; do
					export OMP_NUM_THREADS=1
					str=$(./bin/RKAB_error_alpha.exe dense 10 1E-10 $m $n 2 $k $alpha)
					IFS=' ' read -r -a arr <<< "$str"
					it=${arr[3]}
					./bin/RKAB_max_it_alpha.exe dense 10 $m $n 2 $k $alpha $it >> outputs/omp/RKAB_alpha.txt
					echo "seq $m $n 2 $k $it"
					export OMP_NUM_THREADS=2
					./bin/RKAB_parallel_max_it_alpha.exe dense 10 $m $n $k $alpha $it >> outputs/omp/RKAB_alpha.txt
					echo "par $m $n 2 $k $it"
				done
			done
		fi
	done
done

# 3.99857 não converge para K=500
# 3.99857 não converge para K=1000
# 2.5 3.0 3.99857 não converge para K=4000

N=(4000)
M=(80000)
K=(500 1000 4000)
T=(4)
A=(1.0 1.5 2.0 2.5 3.0 3.99857)

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then
			for k in ${K[@]}; do
				for alpha in ${A[@]}; do
					export OMP_NUM_THREADS=1
					str=$(./bin/RKAB_error_alpha.exe dense 10 1E-10 $m $n 4 $k $alpha)
					IFS=' ' read -r -a arr <<< "$str"
					it=${arr[3]}
					./bin/RKAB_max_it_alpha.exe dense 10 $m $n 4 $k $alpha $it >> outputs/omp/RKAB_alpha.txt
					echo "seq $m $n 4 $k $it"
					export OMP_NUM_THREADS=4
					./bin/RKAB_parallel_max_it_alpha.exe dense 10 $m $n $k $alpha $it >> outputs/omp/RKAB_alpha.txt
					echo "par $m $n 4 $k $it"
				done
			done
		fi
	done
done