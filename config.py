import os
import platform
import flask

class Config:
    ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
    APP_DIR = ROOT_DIR + "/app"
    SECRET_KEY = os.environ.get('SECRET_KEY')
    JWT_SECRET_KEY = 'dasasdds'
    JWT_ACCESS_TOKEN_EXPIRES = 3600

def showBanner(): 
    bannerFile = open(Config.ROOT_DIR + "/banner.txt", "r")
    bannerLog = bannerFile.read()
    bannerFile.close()

    bannerLog = bannerLog.replace("python.version", platform.python_version())
    bannerLog = bannerLog.replace("flask.version", flask.__version__)
    bannerLog = bannerLog.replace("server.path", "/")
    bannerLog = bannerLog.replace("server.port", "5000")

    print(bannerLog)

showBanner()