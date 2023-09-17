from sqlalchemy import create_engine, text
from prefect import flow, task
import pandas as pd
import psycopg2


def get_engine():
    engine = create_engine("postgresql+psycopg2://root:toor@localhost/main_application")
    return engine.connect()


@task(name="Run query in PostgreSQL")
def run_query(query: str) -> None:
    with psycopg2.connect(
        dbname="main_application",
        user="root",
        password="toor",
        host="localhost",
    ) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
        conn.commit()


@task(name="Remove '.' in column names.")
def treat_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.rename(
        columns={
            "alert.action": "alert_action",
            "alert.suricata_id": "alert_suricata_id",
            "alert.signature": "alert_signature",
            "alert.category": "alert_category",
            "alert.severity": "alert_severity",
        }
    )
    df = df.drop(columns="Column1")
    return df


@flow(name="Import dataset to PostgreSQL")
def ingest_json_to_postgres(path: str):
    df = pd.read_json(path)
    df = treat_data(df)

    with get_engine() as conn:
        df.to_sql(name="suricata_logs", con=conn, if_exists="append", index=False)


@flow(name="Main flow", log_prints=True)
def main():
    run_query(query="DROP TABLE IF EXISTS suricata_logs;")
    run_query(
        query="CREATE TABLE suricata_logs ( timestamp TIMESTAMP NULL, flow_id VARCHAR(4000) NULL, in_iface VARCHAR (4000) NULL, event_type VARCHAR (4000) NULL, src_port INTEGER NULL, dest_port INTEGER NULL, proto VARCHAR (4000) NULL, alert VARCHAR (4000) NULL, app_proto VARCHAR (4000) NULL, flow VARCHAR (4000) NULL, stream INTEGER NULL, packet VARCHAR (4000) NULL, packet_info VARCHAR (4000) NULL, tx_id FLOAT NULL, tls VARCHAR (4000) NULL, dns VARCHAR (4000) NULL, metadata VARCHAR (4000) NULL, icmp_type FLOAT NULL, icmp_code FLOAT NULL, http VARCHAR (4000) NULL, tunnel VARCHAR (4000) NULL, alert_action VARCHAR (4000) NULL, alert_suricata_id INTEGER NULL, alert_signature VARCHAR (4000) NULL, alert_category VARCHAR (4000) NULL, alert_severity INTEGER NULL, payload VARCHAR (4000) NULL, src_ip VARCHAR (4000) NULL, dest_ip VARCHAR (4000) NULL, ssh VARCHAR(4000) NULL, smb VARCHAR(4000) NULL );"
    )
    ingest_json_to_postgres("data/Jupyter.json")


if __name__ == "__main__":
    main()
