import csv
import random
from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

def read_csv():
    with open('words.csv', 'r') as file:
        reader = csv.DictReader(file)
        words = list(reader)
    return words

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            num_words = int(request.form['num_words'])
            session['num_words'] = num_words
            return redirect(url_for('word', word_index=0))
        except ValueError:
            flash('Please enter a valid integer.')
    return render_template('index.html')

@app.route('/word/<int:word_index>', methods=['GET', 'POST'])
def word(word_index):
    if word_index >= session['num_words']:
        return redirect(url_for('index'))
    
    words = random.sample(read_csv(), session['num_words'])
    current_word = words[word_index]

    if request.method == 'POST':
        return redirect(url_for('word', word_index=word_index + 1))

    return render_template('word.html', word=current_word, word_index=word_index)

if __name__ == '__main__':
    app.run(debug=True)

