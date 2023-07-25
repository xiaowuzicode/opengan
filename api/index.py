from flask import Flask,request
import openai

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello, World!'
    
@app.route('/about')
def about():
    return 'About'
