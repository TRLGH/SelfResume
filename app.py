from flask import Flask, render_template, jsonify
from database import engine, load_from_db, loads_from_db
from sqlalchemy import text

app = Flask(__name__)

@app.route('/')
def hello_world():
  projects = load_from_db()
  return render_template('home.html',
                         projects=projects)

@app.route("/project/<id>")
def show_project(id):
  projects = loads_from_db(id)
  if not projects:
    return "Not Found", 404
  return render_template('projectpage.html',
                         projects=projects)

@app.route("/api/results")
def list_results():
  result_dict = load_from_db()
  return jsonify(result_dict)

print(__name__)
if __name__ == "__main__":
  app.run('0.0.0.0', debug=True)
