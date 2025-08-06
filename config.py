import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DB_USER = os.getenv("DATABASE_USER")
    DB_PASS = os.getenv("DATABASE_PASS")
    DB_HOST = os.getenv("DATABASE_HOST")
    DB_PORT = os.getenv("DATABASE_PORT")
    DB_NAME = os.getenv("DATABASE_NAME")
    DB_SSLMODE = os.getenv("DATABASE_SSLMODE", "require")
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}?sslmode={DB_SSLMODE}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ENV = os.getenv("FLASK_ENV", "production")