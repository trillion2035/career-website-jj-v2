from flask import Flask, render_template, jsonify

app= Flask(__name__)

JOBS= [
  {
    'id':1,
    'title': 'Data Analyst',
    'location': 'Douala, Cameroon',
    'salary': '350,000 XAF'
  },
   {
    'id':2,
    'title': 'Frontend Engineer',
    'location': 'Lagos, Nigeria',
    'salary': 'N400,000'
  },
  {
    'id':3,
    'title': 'Backend Engineer',
    'location': 'Remote',
    'salary': '$120,000'
  },
]

@app.route("/")
def hello_career():
    return render_template('home.html',jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)