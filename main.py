from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/visitor')
def visitor():
    visitor_num='100'
    return "Visitor: %s" % (visitor_num)
@app.route('/visitor/reset')
def reset_visitor():
    visitor_num='0'
    return "Visitor is reset to %s" % (visitor_num)