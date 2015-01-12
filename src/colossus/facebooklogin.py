from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import request
from facebook import views

apps = Blueprint('apps', __name__)

@apps.route('/')
def index():
	return render_template('fb.html')

@apps.route('/fblogin')
def fb_login():
    return redirect(views.login())

@apps.route('/fapicallback')
def fb_redir():
    return views.check_log(request)

