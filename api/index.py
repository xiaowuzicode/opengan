from flask import Flask,request
import openai
import os

app = Flask(__name__)

@app.route('/chat' methods=['POST'])
def chat():
    user_input = request.form['user_input']
    response = openai.Completion.create(
            model="text-davinci-003",
            prompt=user_input,
            temperature=0.7,
            frequency_penalty=0,
            presence_penalty=0.7,
            max_tokens=240
        )
    return response.choices[0].text.strip()

@app.route('/')
def home():
    return 'Hello, World!'
    
@app.route('/about')
def about():
    return 'About'
