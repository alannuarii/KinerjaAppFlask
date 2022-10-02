from flask import Flask

app = Flask(__name__)

# from app.models import Unit, Spesifikasi, Pengusahaan
from app import routes