from flask import *
from datetime import datetime
import Calculator as calculator
app = Flask(__name__)


@app.route('/')
def index():
    data = "Deploying a Flask App To Heroku"
    return 'hello world!!!!!!!!!!'

if __name__ == '__main__':
    app.run(debug=True)