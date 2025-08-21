import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="library",
        user="postgres",
        password="209209",
        host="localhost",
        port="5432"
    )
