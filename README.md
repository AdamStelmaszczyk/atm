Presentation: https://docs.google.com/presentation/d/1vuZ5K_S_m97DyilThh3fnGVGYhXs51a4V2VwsipGnSg/edit?usp=sharing

## Install

1. Copy the code to your disk: `git clone https://github.com/AdamStelmaszczyk/atm.git`.
2. Change directory to `atm`: `cd atm`.
2. Install [conda](https://conda.io/docs/user-guide/install/index.html).
3. Create conda environment: `conda create -n atm python=3.7.2`.
4. Activate conda environment: `source activate atm`. All the below commands should be run in this environment.
5. Install dependencies: `pip install -r requirements.txt`.

## Run tests

`./manage.py test`

## Run server locally

`./manage.py runserver`

## Query the `/withdraw` endpoint

`curl http://127.0.0.1:8000/withdraw/ --data 'money=280'`

Response:

`[100,100,50,20,10]`