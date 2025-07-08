import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:2004@localhost:5432/mommynme_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False 