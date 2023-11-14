from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

# Connect to the database
engine = create_engine(
  db_connection_string,
        connect_args={
                "ssl": {
                "ssl_ca": "/etc/ssl/cert.pem",
              }
        })

def load_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM projects"))
    result_dict = []
    # db convert to python dict 
    result_dict = [dict(zip(result.keys(), row)) for row in result.fetchall()]
    return result_dict