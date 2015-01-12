from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import request

from google import views

appss = Blueprint('appss', __name__)

@appss.route('/')
def index():
    return render_template('gp.html')

@appss.route('/gplogin')
def gp_login():
    return redirect(views.login())

@appss.route('/gapicallback')
def gp_redir():
    return views.check_login(request)