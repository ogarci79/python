import csv
import random
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            num_words = int(request.form['num_words'])
            if num_words > 0:
                with open('words.csv', newline='') as csvfile:
                    reader = csv.DictReader(csvfile)
                    words = random.sample(list(reader), num_words)
                    return render_template('display.html', words=words)
        except ValueError:
            pass
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

