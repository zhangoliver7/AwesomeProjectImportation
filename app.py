from flask import Flask,render_template,request
from pprint import pprint
import praw, time, webbrowser, json, requests
#pip install praw
#pip install python-oauth2

app = Flask(__name__)

CLIENT_ID = "hF055t0_32EozA"
CLIENT_SECRET = "52QnVb5xvh2HGNHc_af3RXzikrY"
REDIRECT_URI = 'http://127.0.0.1:5000/authorize_callback'

r = praw.Reddit(user_agent='sugoi_app')
#r.login()
#already_done=[]
##we might want to get all subreddits and go further
subreddit = r.get_subreddit("Python")



@app.route('/')
@app.route("/home")
def home():
    text=""
    #access_information = r.get_access_information(code)
    #url = r.get_authorize_url('uniqueKey', 'identity', True)
    #webbrowser.open(url)
    #access_information = r.get_access_information("22CNIdhU1adJnTEOhFL5wLMJfqk")
    #r.set_access_credentials(**access_information)
    #user=r.get_me()
    #print user.name
    #person = r.get_me()
    #print person.name
    ud = dict(request.form.items() + request.args.items())
    if "code" in ud:
        code = ud["code"]
        access_information = r.get_access_information(code)
        r.set_access_credentials(**access_information)
        user=r.get_me()
        print user.name
    else:
        link_refresh = r.get_authorize_url('UniqueKey',
                                       refreshable=True)
        link_refresh = "After doing that, you can enter <a href=%s>here.</a>" % link_refresh
        text = "This requries you to be registered and logged into reddit to work. Head over to <a href='reddit.com'>here</a> and do so first. <br><br>%s</br></br>" % link_refresh
    
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
    logged_link = "<form action='/' method='GET'><input type='hidden' value='"+code+"' name=code><button type='submit'>Return to home</button></form>"
    return render_template("authorize_callback.html",text=variables_text + '</br></br>' + text + '</br></br>' + back_link+"<br><br>"+logged_link)



if __name__=="__main__":
    r = praw.Reddit('OAuth Webserver example by u/_Daimon_ ver 0.1. See '
                    'https://praw.readthedocs.org/en/latest/'
                    'pages/oauth.html for more info.')
    r.set_oauth_app_info(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)
    app.debug=True
    app.run();
