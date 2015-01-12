from flask import redirect, request
import json
import oauth2client.client as oc
import gdata.gauth
import gdata.contacts.client
from models import BaseUser

import os
from . import google_blueprint as app

path  = os.path.abspath(os.path.join(os.path.dirname(__name__),'colossus/google/client_secrets.json'))
print path
flow = oc.flow_from_clientsecrets(path, scope='https://www.google.com/m8/feeds', redirect_uri='http://127.0.0.1:8080/gapicallback')
print "view======---======2"

def login():
    auth_uri = flow.step1_get_authorize_url()
    return auth_uri

def check_login(request):
    code = request.args.get('code')
    print "-----------------"
    if code is None:
        return redirect('/?error=%s' % request.args['error'])
    credentials = flow.step2_exchange(code)


    auth2token = gdata.gauth.OAuth2Token(client_id=credentials.client_id, client_secret=credentials.client_secret, scope='https://www.google.com/m8/feeds/contacts/default/full', access_token=credentials.access_token, refresh_token=credentials.refresh_token, user_agent='sites-test/1.0')
    client = gdata.contacts.client.ContactsClient()
    auth2token.authorize(client)

    query = gdata.contacts.client.ContactsQuery()
    query.max_results = 1000
    feed = client.GetContacts(q = query)

    user=BaseUser()
    for x in feed.entry:
        user.save_user(x, 'google')
    return 'Success : user login with google+'