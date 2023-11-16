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
    projects = [dict(zip(result.keys(), row)) for row in result.fetchall()]
    return projects

def loads_from_db(id):
  with engine.connect() as conn:
    query = text("SELECT * FROM projects WHERE id = :val")
    result = conn.execute(query,
    {"val":id}
    )
    rows = result.fetchone()
    if len(rows) == 0:
      return None
    else:
      return dict(zip(result.keys(), rows))