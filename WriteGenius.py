import openai
import os
from flask import Flask, render_template, request

app = Flask(__name__)


openai.api_key = os.getenv("API_KEY")


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    user_input = request.form['user_input']
    # Process the user input
    messages = [
        {"role": "user", "content": "rewrite the following: hi, I think I have a good way we can increase sales. I reckon if we lower the prices well get more sales."},
        {"role": "assistant", "content": "Greetings, I believe I have a viable solution to boost our sales. In my opinion, reducing the prices would lead to an increase in sales."},
        {"role": "user", "content": f'rewrite the following text to sound polished and refined, but still maintain a conversational tone: {user_input}'},
    ]
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0.3,
        messages=messages,
    )
    reply_content = completion.choices[0].message.content
    return render_template('index.html', reply_content=reply_content)


if __name__ == '__main__':
    app.run(debug=True)
