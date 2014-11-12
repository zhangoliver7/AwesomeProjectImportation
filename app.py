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
    #return template of main.html
    pass

@app.route('/search')
def search():
    #return template of search.html
    pass

@app.route('/results')
def results():
    #return template of results.html
    pass

