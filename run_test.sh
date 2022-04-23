#!/bin/bash
## 02460 FL, template
#BSUB -q hpc 
#BSUB -J CSS ##job name
#BSUB -n 4 ##Number of cores
#BSUB -R "rusage[mem=2048MB]"
#BSUB -R "span[hosts=1]"
#BSUB -M 4GB
#BSUB -W 00:01 ##20 minutes (hh:mm)
#BSUB -N 
#BSUB -o O_CSS_%J.out 
#BSUB -e E_CSS_%J.err 

echo "starting bash script"

module load python3/3.8.0
source /zhome/23/1/141725/Desktop/social_graphs_venv/bin/activate
python content/hej.py