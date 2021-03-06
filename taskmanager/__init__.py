from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("config.ProdConfig")

db = SQLAlchemy(app)

from taskmanager import routes
