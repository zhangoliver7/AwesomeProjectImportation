from flask import Flask,render_template,request
import json
import requests
#from pprint install pprint

app = Flask(__name__)
r = requests.get(r'http://www.reddit.com/user/spilcm/comments/.json')
data = r.json()
print data.keys()

@app.route('/')
def home():
    pass

@app.route('/search')
def search():
    pass

@app.route('results')
def results():
    pass

