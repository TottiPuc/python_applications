from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "this is my first website with flask"

@app.route('/about/')
def about():
    return "this is my secon page of my website with flask"


if __name__ == "__main__":
    app.run(debug=True)