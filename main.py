from flask import Flask, render_template, jsonify
from database import engine
from sqlalchemy import text 

app= Flask(__name__)

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    keys = result.keys()

    jobs = []
    for row in result.fetchall():
        row_dict = dict(zip(keys, row))
        jobs.append(row_dict)
    return jobs

@app.route("/")
def hello_career():
    jobs = load_jobs_from_db()
    return render_template('home.html',
                           jobs=jobs)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)