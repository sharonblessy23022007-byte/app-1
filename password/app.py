from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)

def generate_password(length, letters, numbers, symbols):
    characters = ""

    if letters:
        characters += string.ascii_letters
    if numbers:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    if not characters:
        return "Select at least one option!"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()

    length = int(data.get("length"))
    letters = data.get("letters")
    numbers = data.get("numbers")
    symbols = data.get("symbols")

    password = generate_password(length, letters, numbers, symbols)

    return jsonify({"password": password})


if __name__ == '__main__':
    app.run(debug=True)