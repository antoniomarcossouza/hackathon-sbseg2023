from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)
db_config = {
    "dbname": "main_application",
    "user": "root",
    "password": "toor",
    "host": "localhost",
    "port": "5432",
}


def fetch_data(table_name: str) -> list:
    try:
        with psycopg2.connect(**db_config) as connection:
            with connection.cursor() as cursor:
                query = f"SELECT * FROM {table_name};"
                cursor.execute(query)

                result = cursor.fetchall()
                columns = [desc[0] for desc in cursor.description]

                data = [dict(zip(columns, row)) for row in result]

                return data
    except Exception as e:
        print(f"Error fetching data: {str(e)}")


@app.route("/alerts", methods=["GET"])
def show_alerts():
    return jsonify(fetch_data(table_name="suricata_logs"))


if __name__ == "__main__":
    app.run(debug=True)
