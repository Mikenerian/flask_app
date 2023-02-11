from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    html = render_template('index.html')
    return html

if __name__ == '__main__':
    app.run()
