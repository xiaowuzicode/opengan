from flask import Flask
import request
import openai
import os

    
@app.route('/')
def home():
    return 'Hello, World!'
    
@app.route('/about')
def about():
    return 'About'
