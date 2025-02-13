import os

from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("HOST")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
PORT = os.getenv("PORT")
DATABASE = os.getenv("DATABASE")
DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY =  os.getenv('SECRET_KEY')
ALGORITHM =  os.getenv('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))  # Default to 30 minutes if not set
REFRESH_TOKEN_EXPIRE_DAYS =  os.getenv('REFRESH_TOKEN_EXPIRE_DAYS')