from flask import Flask
from flask import request
import openai

app = Flask(__name__)

openai.api_key = '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'

@app.route('/chat' methods=['POST'])
def chat():
    user_input = request.form['input']
    return 'sdasdschat'
    
@app.route('/')
def home():
    return 'Hello, World!'
    
@app.route('/about')
def about():
    return 'About'
