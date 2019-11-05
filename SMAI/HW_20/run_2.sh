#!/bin/bash
#SBATCH -A RESEARCH
#SBATCH -n 10
#SBATCH --gres=gpu:2
#SBATCH --mem-per-cpu=2048
#SBATCH --time=1-00:00:00
#SBATCH --mail-type=END

module add cuda/10.0
module add cudnn/7-cuda-10.0

# conda activate pytorch

python 2.py 1 0 &
python 2.py 2 1 &
python 2.py 3 1 &
python 2.py 0 0
