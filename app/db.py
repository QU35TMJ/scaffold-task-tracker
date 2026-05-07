import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def get_db_connection(retries=5, delay=2):
    for attempt in range (retries):
        try:

            conn = psycopg2.connect(
                host=os.getenv("DB_HOST"),
                database=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                port=os.getenv("DB_PORT")
            )
            return conn

        except psycopg2.OperationalError as e:
            print(f"Database not ready, retrying...({attempt +1}/{retries})")
            time.sleep(delay)

    raise Exeption("Could not connect database after multiple attempts")
