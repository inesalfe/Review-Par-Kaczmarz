#!/bin/bash

# sbatch bash/mpi/RKA_alpha.sh

#SBATCH --job-name="RKA_alpha"
#SBATCH --output=outputs/progress/RKA_alpha.txt
#SBATCH --time=2-00:00:00
#SBATCH --mem-per-cpu=92GB
#SBATCH --account=urahpc
#SBATCH --partition=cpu1

#SBATCH --nodes=2
#SBATCH --exclusive

module load OpenMPI/4.1.1-GCC-11.2.0

N=(50 100 200 500 750 1000 2000 4000 10000)
M=(2000 4000 20000 40000 80000 160000)
T=(1 2 4 8 12 24 48)

echo "--- Remove Old Files ---"

rm outputs/mpi/RKA_alpha.txt

echo "--- Dense RKA ---"

line=1
for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then	
			for nproc in ${T[@]}; do
				export OMP_NUM_THREADS=1
				str="$(sed "${line}q;d" outputs/mpi/RKA_best_alpha_navg.txt)"
				IFS=' ' read -r -a arr <<< "$str"
				alpha=${arr[3]}
				str="$(sed "${line}q;d" outputs/mpi/RKA_alpha_dist_it_mpi.txt)"
				IFS=' ' read -r -a arr <<< "$str"
				it=${arr[3]}
				srun --nodes=1 --ntasks=1 --ntasks-per-node=1 --cpus-per-task=1 ./bin/RKA_mpi_max_it_alpha_dist.exe dense 10 $m $n $nproc $alpha $it >> outputs/mpi/RKA_alpha.txt
				wait
				echo "seq $m $n $nproc $alpha $it"
				srun --nodes=$(( (nproc + 23) / 24 )) --ntasks=$nproc --ntasks-per-node=$(( nproc < 24 ? nproc : 24 )) --cpus-per-task=1 ./bin/RKA_mpi_parallel_max_it_alpha_dist.exe dense 10 $m $n $alpha $it >> outputs/mpi/RKA_alpha.txt
				wait
				echo "par $m $n $nproc $alpha $it"
				((line++))
			done
		fi
	done
done