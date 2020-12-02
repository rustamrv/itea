from flask import Flask, render_template, jsonify
from manager_db import ManagerDb

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index(): 
    mn_db = ManagerDb()
    rows = mn_db.select_category()  
    return render_template('index.html', categories=rows)


if __name__ == "__main__":
    app.run(debug=True)