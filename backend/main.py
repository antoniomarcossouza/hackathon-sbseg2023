from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)
db_config = {
    "dbname": "main_application",
    "user": "root",
    "password": "toor",
    "host": "localhost",
    "port": "5432",
}

def fetch_data(query:str) -> list:
    try:
        with psycopg2.connect(**db_config) as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)

                result = cursor.fetchall()
                columns = [desc[0] for desc in cursor.description]

                data = [dict(zip(columns, row)) for row in result]

                return data
    except Exception as e:
        print(f"Error fetching data: {str(e)}")

def run_query(query: str) -> None:
    with psycopg2.connect(**db_config) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
        conn.commit()

def whois(ip: str) -> str:
    return f'WhoIs: {ip}'

def check_open_port(ip: str, port: int) -> bool:
    return 0

@app.route("/alertas", methods=["GET", "POST"])
def show_alerts():
    match request.method:
        case "GET":
            return jsonify(fetch_data(query="SELECT * FROM suricata_logs LIMIT 1000;"))
        case "POST":
            json = request.get_json()
            query = f"""
INSERT INTO alerts_responses(
        alert_severity,
        alert_category,
        alert_signature,
        payload,
        src_ip,
        whois_src_ip,
        src_port,
        dest_ip,
        whois_dest_ip,
        dest_port,
        dest_port_open,
        incitent,
        timestamp
    )
VALUES (
        { json ['alert_severity'] },
        '{json['alert_category']}',
        '{json['alert_signature']}',
        '{json['payload']}',
        '{json['src_ip']}',
        '{whois(json['src_ip'])}',
        { json ['src_port'] },
        '{json['dest_ip']}',
        '{whois(json['dest_ip'])}',
        { json ['dest_port'] },
        '{check_open_port(json['dest_port'], json['dest_port'])}',
        { json ['is_incident'] },
        '{json['timestamp']}'
    );"""
            try:
                run_query(query=query)
                if json['is_incident']:
                    print('Envia request para Request Tracker')
                return "Success", 200
            except Exception as e:
                return "Internal Server Error", 500

@app.route('/incidentes', methods=['GET'])
def get_incidents():
    return jsonify(fetch_data("SELECT * FROM alerts_responses WHERE incitent IS TRUE;"))

if __name__ == "__main__":
    app.run(debug=True)
