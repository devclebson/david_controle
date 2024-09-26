from flask import Blueprint, render_template, url_for, session, redirect, request
from functools import wraps



bp_home = Blueprint('home', __name__, url_prefix='/', template_folder='templates')

@bp_home.route("/", methods=['GET', 'POST'])
def homePage():    
    return render_template("site.html")

