from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem",
                       }})


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
  with engine.connect() as conn:
    s = text("select * from jobs where id = :val")
    result = conn.execute(s, {"val": id})
    row = result.fetchone()

    if row is None:
      return None

    # Convert the row to a dictionary using _asdict() method
    return row._asdict()


def add_application_to_db(job_id, application):
  with engine.connect() as conn:
    query = text("""
            INSERT INTO applications 
            (job_id, full_name, email, linkedin_url, education,                 work_experience, resume_url) 
            VALUES (:job_id, :full_name, :email, :linkedin_url,                 :education, :work_experience, :resume_url)
            """)

    params = {
      "job_id": job_id,
      "full_name": application['full_name'],
      "email": application['email'],
      "linkedin_url":
      application.get('linkedin_url',
                      None),  # using .get() to handle missing keys gracefully
      "education": application.get('education', None),
      "work_experience": application.get('work_experience', None),
      "resume_url": application.get('resume_url', None)
    }

    conn.execute(query, params)


#def add_application_to_db(job_id, application):
#  with engine.connect() as conn:
#   query = text("INSERT INTO applications (job_id, full_name, email, linkdedin_url, education, work_experience, resume_url) VALUES (: job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)" )

# conn.execute(query,
#             job_id=job_id,
#            full_name=application['full_name'],
#           email=application['email'],
#           linkedin_url=application['linkedin_url'],
#           education=application['education'],
#          work_experience=application['work_experience'],
#          resume_url=application['resume_url'])
