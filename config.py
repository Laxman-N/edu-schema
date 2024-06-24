import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:Sathya143#@localhost/EduSchema'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
