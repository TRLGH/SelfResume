from flask import Flask, render_template, jsonify
from database import load_from_db

app = Flask(__name__)

@app.route('/')
def hello_world():
  result_dict = load_from_db()
  return render_template('home.html',
                         results=result_dict,
                         company_name='Jovian')



@app.route("/api/results")
def list_results():
  result_dict = load_from_db()
  return jsonify(result_dict)

print(__name__)
if __name__ == "__main__":
  app.run('0.0.0.0', debug=True)
