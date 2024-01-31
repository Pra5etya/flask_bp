from flask import Flask

app = Flask(__name__)

# Import blueprint
from web_app.main.views import main_blueprint
from web_app.auth.views import auth_blueprint

# Register blueprint
app.register_blueprint(main_blueprint)
app.register_blueprint(auth_blueprint)
