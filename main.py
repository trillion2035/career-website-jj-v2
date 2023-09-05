from flask import Flask, render_template, jsonify
from database import load_jobs_from_db
from sqlalchemy import text 

app= Flask(__name__)

@app.route("/")
def hello_career():
    jobs = load_jobs_from_db()
    return render_template('home.html',
                           jobs=jobs)

@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)

@app.route("/jobs/<id>")
def show_job(id):
  job = load_job_from_db(id)
  return jsonify(job)
  

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)