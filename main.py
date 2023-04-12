from flask import Flask, render_template

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('index.html', name='Diego')


if __name__ == '__main__':
    app.run()

