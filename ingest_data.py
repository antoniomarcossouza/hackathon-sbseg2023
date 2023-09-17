from sqlalchemy import create_engine, text
from prefect import flow, task
from dotenv import load_dotenv
import pandas as pd
import os


@task(name="Run query in PostgreSQL")
def run_query(query: str) -> None:
    engine = create_engine(os.environ.get("URL"))

    with engine.connect() as conn:
        sql_query = text()
        conn.execute(sql_query)


@flow(name="Import dataset to PostgreSQL")
def ingest_json_to_postgres(path: str):
    df = pd.read_json(path)


@flow(name="Main flow", log_prints=True)
def main():
    run_query(
        query=""""
            CREATE TABLE accounts (
        timestamp DATETIME64 (4000) NULL,
        flow_id OBJECT (4000) NULL,
        in_iface VARCHAR (4000) NULL,
        event_type VARCHAR (4000) NULL,
        src_port VARCHAR (4000) NULL,
        dest_port VARCHAR (4000) NULL,
        proto VARCHAR (4000) NULL,
        alert VARCHAR (4000) NULL,
        app_proto VARCHAR (4000) NULL,
        flow VARCHAR (4000) NULL,
        stream VARCHAR (4000) NULL,
        packet VARCHAR (4000) NULL,
        packet_info VARCHAR (4000) NULL,
        tx_id VARCHAR (4000) NULL,
        tls VARCHAR (4000) NULL,
        dns VARCHAR (4000) NULL,
        metadata VARCHAR (4000) NULL,
        icmp_type VARCHAR (4000) NULL,
        icmp_code VARCHAR (4000) NULL,
        http VARCHAR (4000) NULL,
        tunnel VARCHAR (4000) NULL,
        alert.action VARCHAR (4000) NULL,
        alert.suricata_id VARCHAR (4000) NULL,
        alert.signature VARCHAR (4000) NULL,
        alert.category VARCHAR (4000) NULL,
        alert.severity VARCHAR (4000) NULL,
        payload VARCHAR (4000) NULL,
        src_ip VARCHAR (4000) NULL,
        dest_ip VARCHAR (4000) NULL
    );"""
    )
    ingest_json_to_postgres("data/Venus.json")


if __name__ == "__main__":
    load_dotenv()
    main()
