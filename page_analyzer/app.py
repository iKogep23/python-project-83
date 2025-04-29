from flask import Flask, request, render_template, url_for
from dotenv import load_dotenv
import os
import psycopg2


app = Flask(__name__)


load_dotenv()
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
#DATABASE_URL = os.getenv('DATABASE_URL')
#conn = psycopg2.connect(DATABASE_URL)


@app.route('/')
def index():
    return render_template (
        'index.html'
    )


@app.route('/urls')
def urls():
    urls = []
    list_of_urls = get_DB_list_of_urls()
    urls = get_urls(list_of_urls)
    return render_template(
        'urls.html',
        urls=urls
    )
