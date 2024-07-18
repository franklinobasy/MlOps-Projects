## MLflow

- [Documentation](https://mlflow.org/docs/latest/index.html)

- [MLflow tutorial](https://youtube.com/playlist?list=PLkz_y24mlSJZrqiZ4_cLUiP0CBN5wFmTb&si=zEp_C8zLHt1DzWKK)

##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/franklinobasy/MlOps-Projects.mlflow \
MLFLOW_TRACKING_USERNAME=franklinobasy \
MLFLOW_TRACKING_PASSWORD=6824692c47a4545eac5b10041d5c8edbcef0 \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/franklinobasy/MlOps-Projects.mlflow

export MLFLOW_TRACKING_USERNAME=franklinobasy

export MLFLOW_TRACKING_PASSWORD=5bf8980ce5b4b7db68e62dabb427bd11b0381dca

```

### AWS
bucket-url = 's3://mymlflowproject-buc01'
Run this command in ec2 instance: mlflow server -h 0.0.0.0 --default-artifact-root s3://mymlflowproject-buc01

--in local terminal
export MLFLOW_TRACKING_URI=http://ec2-44-206-252-28.compute-1.amazonaws.com:5000/
