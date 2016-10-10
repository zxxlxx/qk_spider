import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '\xfbT#4\x87T\xa4\x8cS\xee\xdc\xca}\xd1\x12\x96fe\xaf,ij\xdd\xa8'
    SSL_DISABLE = False
