import os
import platform
import importlib.metadata

class Config:
    ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
    APP_DIR = ROOT_DIR + "/app"
    SECRET_KEY = os.environ.get('SECRET_KEY')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = 3600
    SWAGGER_URL = '/swagger-ui'
    SWAGGER_FILE = "/static/swagger.yml"

def showBanner(): 
    bannerFile = open(Config.ROOT_DIR + "/banner.txt", "r")
    bannerLog = bannerFile.read()
    bannerFile.close()

    bannerLog = bannerLog.replace("python.version", platform.python_version())
    bannerLog = bannerLog.replace("flask.version", importlib.metadata.version("flask"))
    bannerLog = bannerLog.replace("server.path", "/")
    bannerLog = bannerLog.replace("server.port", "5000")

    print(bannerLog)

showBanner()