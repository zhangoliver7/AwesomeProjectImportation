from flask import Flask,render_template,request
import json
import requests
from pprint import pprint
import praw
import webbrowser
#pip install praw
#pip install python-oauth2

app = Flask(__name__)

CLIENT_ID = "hF055t0_32EozA"
CLIENT_SECRET = "52QnVb5xvh2HGNHc_af3RXzikrY"
REDIRECT_URI = 'http://127.0.0.1:5000/authorize_callback'

##r = praw.Reddit(user_agent='sugoi_app')
##we might want to get all subreddits and go further
##subreddit = r.get_subreddit("Python")

@app.route('/')
@app.route("/home")
def home():
    link_no_refresh = r.get_authorize_url('UniqueKey')
    link_no_refresh = "<a href=%s>link</a>" % link_no_refresh
    text = "First link. Not refreshable %s</br></br>" % link_no_refresh
    return render_template("home.html",text=text)

@app.route('/authorize_callback')
def authorized():
    state = request.args.get('state', '')
    code = request.args.get('code', '')
    info = r.get_access_information(code)
    user = r.get_me()
    variables_text = "State=%s, code=%s, info=%s." % (state, code,
                                                      str(info))
    text = 'You are %s and have %u link karma.' % (user.name,
                                                   user.link_karma)
    back_link = "<a href='/'>Try again</a>"
    return render_template("authorize_callback.html",text=variables_text + '</br></br>' + text + '</br></br>' + back_link)



if __name__=="__main__":
    r = praw.Reddit('OAuth Webserver example by u/_Daimon_ ver 0.1. See '
                    'https://praw.readthedocs.org/en/latest/'
                    'pages/oauth.html for more info.')
    r.set_oauth_app_info(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)
    app.debug=True
    app.run();
