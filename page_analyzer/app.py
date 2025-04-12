from flask import Flask, request
from dotenv import load_dotenv

# Это callable WSGI-приложение
app = Flask(__name__)


load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

