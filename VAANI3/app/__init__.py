from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Import routes after initializing the app
from app import routes