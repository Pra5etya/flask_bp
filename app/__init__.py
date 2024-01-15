# app/__init__.py
from flask import Flask

app = Flask(__name__)

# Import blueprint
from app.main.views import main_blueprint
from app.auth.views import auth_blueprint

# Register blueprint
app.register_blueprint(main_blueprint)
app.register_blueprint(auth_blueprint)
