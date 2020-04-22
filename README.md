# Log monitoring 

This is a Flask based web application for logging and monitoring failed Airflow DAGs

## Install Python
The project uses `python3.6.0`.

```bash
python --version
```

Usage of `virtualenv` is highly recommended for managing isolated python environments. 

Refer https://github.com/pypa/virtualenv


## Install python dependencies
- gcsfs==0.6.1
- pandas==0.25.3
- google-cloud-bigquery==1.24.0
- oauth2client==4.1.3
- dask==2.14.0

To install the dependencies, run

```bash
pip install -r requirements.txt
```

