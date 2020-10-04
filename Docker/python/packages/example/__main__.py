from sqlalchemy import create_engine
from flask import Flask, render_template, request

app = Flask(__name__)
engine = create_engine('mysql://dev:dev@mysql/sample_db?charset=utf8')

@app.route("/", methods=["GET"])
def main_page():
    return render_template("layout.html")


app.run(host='0.0.0.0', port=5000, debug=True)