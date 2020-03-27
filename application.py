from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# Import table definitions.
from models import *

app = Flask(__name__)

# Tell Flask what SQLAlchemy databas to use.
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://knvokdgxqextah:194949a836908f9186232baafb3ec287dd273b35772bccb56e2e69cd5802d174@ec2-34-200-101-236.compute-1.amazonaws.com:5432/d5ilo34jg2civm"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route("/")
def index():
    return "Hello, world!"