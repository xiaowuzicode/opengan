from flask import Flask
from flask import request
import openai

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'
    
@app.route('/about')
def about():
    return 'About'


@app.route('/chat' methods=['POST'])
def chat():
    user_input = request.form['input']
    response = openai.Completion.create(
        engine='text-davinci-003'
        prompt=user_input
        max_tokens=50
        temperature=0.7
        n=1
        stop=None
        temperature=0.7
    )
    return response.choices[0].text.strip()
