import psycopg2
from psycopg2 import OperationalError

def get_db_connection():
    DB_NAME = "cc"
    DB_USER = "postgres"
    DB_PASS = "800122"
    DB_HOST = "localhost"
    DB_PORT = "5432"
    try:
        connection = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
        print("Connected to the database.")
        return connection
    except OperationalError as e:
        print(f"An error occurred while connecting to the database: {e}")
    except Exception as e:
        
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    connection = get_db_connection()
    if connection is not None:
        print("Connection successful!")
    else:
        print("Connection failed.")
