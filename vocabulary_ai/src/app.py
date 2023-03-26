from flask import Flask, render_template, request
import csv
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/next', methods=['POST'])
def next_word():
    current_index = int(request.form['current_index'])
    word_list = []
    with open('words.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            word_list.append(row)
    next_word_index = (current_index + 1) % len(word_list)
    next_word = word_list[next_word_index]
    return next_word

if __name__ == '__main__':
    app.run(debug=True)

