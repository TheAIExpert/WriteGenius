import openai
import os
from flask import Flask, render_template, request

app = Flask(__name__)


openai.api_key = os.getenv("API_KEY")


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form['user_input']
    # Submit the user input
    messages = [
        {"role": "user", "content": f'rewrite the following: {user_input}'},
    ]
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0.4,
        messages=messages,
    )
    reply_content = completion.choices[0].message.content
    return render_template('index.html', reply_content=reply_content)


if __name__ == '__main__':
    app.run(debug=True)
