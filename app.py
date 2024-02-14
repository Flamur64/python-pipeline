from flask import Flask

app = Flask(__name__)

@app.route('/')
def hallo():
    return 'Flask App von Flamur'

if __name__ == '__main__':
    app.run(debug=True)
