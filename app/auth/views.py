# app/auth/views.py
from flask import Blueprint, render_template
from app.auth import views

auth_blueprint = Blueprint('auth', __name__, template_folder = 'templates')

@auth_blueprint.route('/login')
def login():
    return render_template('auth/login.html')