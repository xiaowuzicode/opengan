from flask import Flask,request
import openai
import os

    
@app.route('/')
def home():
    return 'Hello, World!'
    
@app.route('/about')
def about():
    return 'About'


if __name__ == "__main__":
    app.run()
