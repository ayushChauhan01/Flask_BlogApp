from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

#This is the place where we will initialise the blog app.
# CREATE A FLASK INSTANCE
app = Flask(__name__, template_folder='templates')
#ADD DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# #SECRET KEY!
app.config['SECRET_KEY'] = "7a51b6b0a542ca504e80dbb9c25733b1"
# #INITIALIZE THE DATABASE
db = SQLAlchemy(app)
app.app_context().push()
bcrypt = Bcrypt(app)
login_manager = LoginManger(app)


from flask_blog import routes