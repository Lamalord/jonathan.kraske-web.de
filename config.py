import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'youwillnevergues'
    SQLALCHEMY_DATABASE_URI = 'postgres://aginzfhurjnpib:f07b3f6ef963a7eaa216d1c9580cec44ef5c7a6c00dd8fb83d24d18ae0a6d4f5@ec2-18-215-99-63.compute-1.amazonaws.com:5432/dtcf4s44m3fjl'
    SQLALCHEMY_TRACK_MODIFICATIONS = False