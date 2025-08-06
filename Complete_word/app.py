from flask import Flask, render_template, request, jsonify
import nltk
from nltk.corpus import words

nltk.download('words')
english_words = set(words.words())

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validate_word', methods=['POST'])
def validate_word():
    data = request.get_json()
    word = data.get('word', '').lower()
    is_valid = word in english_words if len(word) >= 4 else True
    return jsonify({'valid': is_valid})

if __name__ == '__main__':
    app.run(debug=True)