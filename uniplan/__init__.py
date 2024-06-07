import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db-jun724.db'
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")


db = SQLAlchemy(app=app)

from uniplan import routes