"""Flask configuration."""
from dotenv import load_dotenv
import os

load_dotenv('.env')
SECRET_KEY = os.environ.get('SECRET_KEY')
DATABASE_URL = os.environ.get('DATABASE_URL')
DEBUG = True
TESTING = True

