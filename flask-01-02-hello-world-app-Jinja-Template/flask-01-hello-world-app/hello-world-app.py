from flask import Flask 


app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hello World</h1>"

@app.route('/second')
def second():
    return "This is the second page</h2>"


if __name__ == '__main__':
    app.run(debug=False)

@app.route('/third/subthird')
def third():
    return "This is the subpage of the third page"



