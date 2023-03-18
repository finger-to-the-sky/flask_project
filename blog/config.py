import os
from dotenv import load_dotenv

load_dotenv()
FLASK_DEBUG = os.getenv('FLASK_DEBUG')
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
SECRET_KEY = os.getenv('SECRET_KEY')