from flask import Blueprint, render_template

auth_blueprint = Blueprint('auth', __name__, template_folder = 'templates', static_folder = 'static')

@auth_blueprint.route('/login')
def login():
    return render_template('sample2.html')