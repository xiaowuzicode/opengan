from flask import Flask render_template request
import openai

app = Flask(__name__)

openai.api_key = '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'

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
