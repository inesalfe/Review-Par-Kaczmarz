#!/bin/bash

# sbatch bash/mpi/RKAB_mpi.sh

#SBATCH --job-name="RKAB_mpi"
#SBATCH --output=outputs/progress/RKAB_mpi.txt
#SBATCH --time=2-00:00:00
#SBATCH --mem-per-cpu=92GB
#SBATCH --account=urahpc
#SBATCH --partition=cpu1

#SBATCH --nodes=2
#SBATCH --exclusive

module load OpenMPI/4.1.1-GCC-11.2.0

# N=(1000 4000 10000)
# M=(4000 20000 40000 80000 160000)
# K=(5 10 100 500 1000 2000 4000 10000)
# T=(1 2 4 8 12 24 48)

# echo "--- Remove Old Files ---"

# rm outputs/mpi/RKAB_mpi.txt

# echo "--- Dense RKAB ---"

# line=1
# for m in ${M[@]}; do
# 	for n in ${N[@]}; do
# 		if [ "$m" -gt "$(( 2*n ))" ]
# 		then
# 			for k in ${K[@]}; do
# 				for nproc in ${T[@]}; do
# 					export OMP_NUM_THREADS=1
# 					str="$(sed "${line}q;d" outputs/mpi/RKAB_dist_it_mpi.txt)"
# 					IFS=' ' read -r -a arr <<< "$str"
# 					it=${arr[3]}
# 					srun --nodes=1 --ntasks=1 --ntasks-per-node=1 --cpus-per-task=1 ./bin/RKAB_mpi_max_it_dist.exe dense 10 $m $n $nproc $k $it >> outputs/mpi/RKAB_mpi.txt
# 					wait
# 					echo "seq $m $n $nproc $it"
# 					srun --nodes=$(( (nproc + 23) / 24 )) --ntasks=$nproc --ntasks-per-node=$(( nproc < 24 ? nproc : 24 )) --cpus-per-task=1 ./bin/RKAB_mpi_parallel_max_it_dist.exe dense 10 $m $n $k $it >> outputs/mpi/RKAB_mpi.txt
# 					wait
# 					echo "par $m $n $nproc $it"
# 					((line++))
# 				done
# 			done
# 		fi
# 	done
# done

echo "--- Dense RKAB ---"

N=(10000)
M=(80000)
K=(10000)
T=(48)

line=504
for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then
			for k in ${K[@]}; do
				for nproc in ${T[@]}; do
					export OMP_NUM_THREADS=1
					str="$(sed "${line}q;d" outputs/mpi/RKAB_dist_it_mpi.txt)"
					IFS=' ' read -r -a arr <<< "$str"
					it=${arr[3]}
					srun --nodes=1 --ntasks=1 --ntasks-per-node=1 --cpus-per-task=1 ./bin/RKAB_mpi_max_it_dist.exe dense 10 $m $n $nproc $k $it >> outputs/mpi/RKAB_mpi.txt
					wait
					echo "seq $m $n $nproc $it"
					srun --nodes=$(( (nproc + 23) / 24 )) --ntasks=$nproc --ntasks-per-node=$(( nproc < 24 ? nproc : 24 )) --cpus-per-task=1 ./bin/RKAB_mpi_parallel_max_it_dist.exe dense 10 $m $n $k $it >> outputs/mpi/RKAB_mpi.txt
					wait
					echo "par $m $n $nproc $it"
					((line++))
				done
			done
		fi
	done
done

N=(1000 4000 10000)
M=(160000)
K=(5 10 100 500 1000 2000 4000 10000)
T=(1 2 4 8 12 24 48)

line=505
for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then
			for k in ${K[@]}; do
				for nproc in ${T[@]}; do
					export OMP_NUM_THREADS=1
					str="$(sed "${line}q;d" outputs/mpi/RKAB_dist_it_mpi.txt)"
					IFS=' ' read -r -a arr <<< "$str"
					it=${arr[3]}
					srun --nodes=1 --ntasks=1 --ntasks-per-node=1 --cpus-per-task=1 ./bin/RKAB_mpi_max_it_dist.exe dense 10 $m $n $nproc $k $it >> outputs/mpi/RKAB_mpi.txt
					wait
					echo "seq $m $n $nproc $it"
					srun --nodes=$(( (nproc + 23) / 24 )) --ntasks=$nproc --ntasks-per-node=$(( nproc < 24 ? nproc : 24 )) --cpus-per-task=1 ./bin/RKAB_mpi_parallel_max_it_dist.exe dense 10 $m $n $k $it >> outputs/mpi/RKAB_mpi.txt
					wait
					echo "par $m $n $nproc $it"
					((line++))
				done
			done
		fi
	done
done