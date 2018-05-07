#!/bin/bash -l
#SBATCH -p debug
#SBATCH -t 1

module load anaconda3

srun ./split.py

idapply=$(sbatch --dependency=afterok:${SLURM_JOB_ID} \
--array=1-$(wc -l cats.txt|perl -lane 'print $F[0]') \
apply.sh | perl -lane 'print $F[3]')

sbatch --dependency=afterok:${idapply} combine.sh
