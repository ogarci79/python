import csv
import random
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num_words = int(request.form['num_words'])
        with open('words.csv') as f:
            reader = csv.DictReader(f)
            words = random.sample(list(reader), num_words)
            return render_template('words.html', words=words)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

