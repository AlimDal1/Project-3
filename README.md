# Project-3
│
├── airflow/
│   └── dags/
│       └── etl_pipeline.py
│
├── config/
│   └── config.yaml
│
├── data/
│   ├── raw/
│   └── processed/
│
├── database/
│   └── data.db
│
├── logs/
│
├── src/
│   ├── extract/
│   │   ├── from_csv.py
│   │   ├── from_api.py
│   │   └── from_web.py
│   ├── transform/
│   │   └── clean.py
│   ├── load/
│   │   └── to_db.py
│   ├── validate/
│   │   └── validate.py
│   └── utils/
│       └── logger.py
│
├── dashboard/
│   └── app.py
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
