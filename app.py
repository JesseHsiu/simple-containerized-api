from flask import Flask, abort
from time import sleep
import random

app = Flask(__name__)

@app.route('/')
def health_check():
    return f'ok'

@app.route('/good-api')
def good_api():
    return f'good-api'

@app.route('/error-api')
def error_api():
    abort(400)

@app.route('/slow-api')
def slow_api():
    sleep(random.uniform(1, 2))
    return f'slow-api'