echo [$(date)]: "START" 
echo [$(date)]: "creating env with python 3.8 version" 
conda create --prefix ./env python=3.8 -y
echo [$(date)]: "activating the environment" 
source activate ./env
echo [$(date)]: "installing the dev requirements" 
pip install -r requirements_dev.txt
echo [$(date)]: "installing pytorch version 1.8.1" 
conda install pytorch==1.8.1 cudatoolkit=11.3 -c pytorch -c conda-forge
echo [$(date)]: "END"