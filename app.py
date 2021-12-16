from flask import Flask
# New instance of flask called app
app = Flask(__name__)
#Create Route Root
@app.route('/')
def hello_world():
    return 'Hello world'

