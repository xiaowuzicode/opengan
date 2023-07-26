from flask import Flask,request,jsonify
import openai
import os

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

def Response_headers(content):  
    resp = Response(content)  
    resp.headers['Access-Control-Allow-Origin'] = '*'  
    return resp


@app.route('/chat',methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data['userInput']
    userPassword = data['userPassword']
    response = openai.Completion.create(
            model="text-davinci-003",
            prompt=user_input,
            temperature=0.7,
            frequency_penalty=0,
            presence_penalty=0.7,
            max_tokens=240
    )
    content = response.choices[0].text.strip()
    resp = Response_headers(content)  
    return resp

@app.route('/test',methods=["POST"])
def test():
    data = request.get_json(force=True)
    return data +"123---"

@app.route('/')
def home():
    return 'Hello, World!'
    
@app.route('/about')
def about():
    return 'About'
