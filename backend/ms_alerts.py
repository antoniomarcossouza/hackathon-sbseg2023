"""Microsservice that handles the alerts."""
from flask import Flask, request, jsonify

from PostgreSQL import PostgreSQL

app = Flask(__name__)
database = PostgreSQL()


@app.route("/alerts", methods=["GET", "POST"])
def alerts():
    """Alerts endpoint."""
    match request.method:
        case "POST":
            # Send to Priority evaluation endpoint
            # Send to Alert evaluation endpoint
            # INSERT query on README.md
            pass
        case "GET":
            return jsonify(database.select_query(query="SELECT * FROM alerts LIMIT 1000;")), 200
