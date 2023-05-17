from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)
openai.api_key = os.environ.get('API_KEY')


@app.route('/')
def home():
    return render_template('WriteGenius.html')


@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form['user_input']
    option = request.form['option']
    # Submit the user input
    if option == 'option1':
        messages = [
            {"role": "user",
            "content": f'Please rewrite the following text: {user_input}'},
        ]
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature=0.5,
            messages=messages,
    )
        
    elif option == 'option2':
        messages = [
            {"role": "user",
            "content": f'Capture the essence of a highly influential and enthusiastic social media personality known for their captivating storytelling. Rewrite the following paragraph in a way that emulates their style and keep it brief. Include emojis if suitable and five hashtags: {user_input}'},
        ]
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature=0.5,
            messages=messages,
    )
    reply_content = completion.choices[0].message.content
    return render_template('WriteGenius.html', reply_content=reply_content)
    

if __name__ == '__main__':
    app.run(debug=True)