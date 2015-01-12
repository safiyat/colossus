from . import face
from flask import Flask, redirect, request, url_for
import requests
from flask_oauth import OAuth
import oauth2client.client as oc
oauth = OAuth()

from flask import Blueprint
from . import face

app = Blueprint('app', __name__)

credentials = None

facebook = oauth.remote_app('facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key='1541474329457751',
    consumer_secret='fae94898a591206d32856cd02dc6cc4f',
    request_token_params={'scope': 'email'}
)
import json
app = Flask(__name__)
print "3333333333"

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    data = facebook.authorize(callback=url_for('facebook_authorized',
        next=request.args.get('next') or request.referrer or None,
        _external=True))
    print data
    return data

# print data



# def login():
#     auth_uri = 'https://www.facebook.com/dialog/oauth?client_id=' + APP_ID + '&redirect_uri=' + REDIRECT_URI
#     print "hhw========================="
#     print auth_uri
#     return redirect(auth_uri)

# def check_log(request):
#     error = request.args.get('error')
#     if error is not None:
#         return 'invalid login'
#     code = request.args.get('code')
#     print " === "+str(code)
#     print "+++"+ request.content
#     print "llll"+REDIRECT_URI
#     # req = 'https://graph.facebook.com/oauth/access_token?client_id=' + APP_ID + '&redirect_uri=' + REDIRECT_URI + '&client_secret=' + APP_SECRET + '&code=' + code
#     # response = requests.get(req).content
#     # if response.startswith('access_token'):
#     #     start = 13
#     #     end = response.find('expires', start) - 1
#     #     access_token = response[start:end]
#     #     req = 'https://graph.facebook.com/v2.2/me/friends?fields=name&access_token=' + access_token
#     #     req = 'https://graph.facebook.com/v2.2/me/taggable_friends?fields=name&access_token=' + access_token
#     #     req = 'https://graph.facebook.com/v2.2/me/friends?fields=id,name,picture.type(large)&access_token=' + access_token
#     #     req = 'https://graph.facebook.com/v2.2/me/taggable_friends?fields=name,picture.type(large)&access_token=' + access_token
#     #     k = requests.get(req)
#     #     temp = k.content
#     # else:
#     return 'Error'

