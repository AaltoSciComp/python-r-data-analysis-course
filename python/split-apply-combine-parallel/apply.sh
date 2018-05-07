#!/bin/bash -l
#SBATCH -p debug
#SBATCH -t 1

module load anaconda3
srun ./apply.py $SLURM_ARRAY_TASK_ID
