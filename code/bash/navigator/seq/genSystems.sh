#!/bin/bash

# sbatch bash/seq/genSystems.sh

#SBATCH --job-name="genSystems"
#SBATCH --output=outputs/progress/genSystems.txt
#SBATCH --time=1-00:00:00
#SBATCH --mem-per-cpu=92GB
#SBATCH --account=urahpc
#SBATCH --partition=cpu1

#SBATCH --nodes=1
#SBATCH --exclusive

module load GCC/11.2.0

./bin/genConsistDataSets.exe
# ./bin/genLSDataSets.exe