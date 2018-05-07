#!/bin/bash -l
#SBATCH -p debug
#SBATCH -t 1

module load anaconda3
srun ./combine.py
