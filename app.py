from flask import Flask, render_template,jsonify

app = Flask(__name__)


JOBS = [
    {
      'id':1,
      'title':'Data Analyst',
      'location':'New York',
      'salary':'1000000 reais'
    },
    {
      'id':2,
      'title':'Data Scientist',
      'location':'New York',
      'salary':'1000000 reais'
    },
    {
      'id':3,
      'title':'Data data',
      'location':'NYC',
      'salary':'100000'
  }
]

@app.route('/')
def hello_world():
  return render_template('home.html',
                         jobs=JOBS,
                         company_name='Jovian')



@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)
  
print(__name__)
if __name__ == "__main__":
  app.run('0.0.0.0', debug=True)
