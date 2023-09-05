from sqlalchemy import create_engine, text
import os

db_connection_string= os.environ['DB_CONNECTION_STRING']

engine = create_engine(
  db_connection_string,
  connect_args={
     "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem",
        }
  })

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    keys = result.keys()

    jobs = []
    for row in result.fetchall():
        row_dict = dict(zip(keys, row))
        jobs.append(row_dict)
    return jobs


def load_job_from_db(id):
  if not id
    return None
  
  with engine.connect() as conn:
    result=conn.execute(
      text("select * from jobs where id = :val"),
      val=id
    )
    
    rows = result.fetchone()
    if row is None:
      return None

    return dict(row)