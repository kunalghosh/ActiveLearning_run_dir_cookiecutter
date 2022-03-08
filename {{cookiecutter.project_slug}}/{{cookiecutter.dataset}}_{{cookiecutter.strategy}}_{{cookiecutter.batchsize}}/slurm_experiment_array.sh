#!/bin/bash
#SBATCH --job-name={{cookiecutter.dataset}}-{{cookiecutter.strategy}}-{{cookiecutter.batchsize}}
#SBATCH --account=project_2000382
#SBATCH --time=72:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=20
#SBATCH --mem-per-cpu=5G
#SBATCH --partition=small
#SBATCH --array=1-5
#SBATCH --output=activeLearning-A-EXP_%a.out

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

module load python-data/3.7.6-1
export PROJAPPL=/projappl/project_2000382

if [ ! -d "run$SLURM_ARRAY_TASK_ID" ]; then
    # directory doesn't exist
    echo "run directories don't exist exitting !"
    exit 1
fi

cd run$SLURM_ARRAY_TASK_ID
srun ../main_test.sh run$SLURM_ARRAY_TASK_ID input.dat
