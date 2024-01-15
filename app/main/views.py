# app/main/views.py
from flask import Blueprint, render_template
from app.main import views

main_blueprint = Blueprint('main', __name__, template_folder = 'templates')

@main_blueprint.route('/')
def index():
    return render_template('main/main.html')
