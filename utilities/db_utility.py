import mysql.connector


class DbUtility:

    @staticmethod
    def get_connection(host, port, db_name, username, password):
        return mysql.connector.connect(
            host=host, port=port,
            database=db_name, user=username,
            password=password
        )

    @staticmethod
    def execute_query(connection, query):
        cursor = connection.cursor(
            dictionary=True
        )

        cursor.execute(
            query
        )

        return cursor.fetchall()
