"""Class to encapsulate the connection to the Postgres database."""
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


class PostgreSQL:
    """Class to encapsulate the connection to the Postgres database."""

    def __init__(self):
        """Constructor for the PostgreSQL class."""
        self.__conn = psycopg2.connect(os.environ.get("POSTGRES_URL"))
        self.__cursor = self.__conn.cursor()

    def select_query(self, query: str):
        """Executes a SELECT query on the Postgres database.

        args
        ----
            query : str
                The query to execute.

        returns
        ------
            A list of dictionaries representing the rows returned by the query."""
        self.__cursor.execute(query)
        return [
            dict(zip([column[0] for column in self.__cursor.description], row))
            for row in self.__cursor.fetchall()
        ]

    def action_query(self, query: str):
        """Executes an action query on the Postgres database.

        args
        ----
            query : str
                The query to execute.
        """
        self.__cursor.execute(query)
        self.__conn.commit()
