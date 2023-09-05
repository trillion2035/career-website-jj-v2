from sqlalchemy import create_engine, text

db_connection_string= "mysql+pymysql://z4l4xfs6ur3xb5p2ea7y:pscale_pw_J7SlUmiEiiEWrGoqVsaJsbBsXvISvCYpLmwRKvCyRT3@aws.connect.psdb.cloud/careerwebsite?charset=utf8mb4"

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