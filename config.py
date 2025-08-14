import os
import platform
import importlib.metadata

class Config:
    ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
    APP_DIR = ROOT_DIR + "/app"
    SERVER_PATH = "/"
    SERVER_PORT = 5000
    SECRET_KEY = os.environ.get('SECRET_KEY')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = 3600
    SWAGGER_URL = '/swagger-ui'
    SWAGGER_FILE = "/static/swagger.yml"
    TITLE = "Python Flask"
    VERSION = "1.0.0"

def showBanner(): 
    bannerFile = open(Config.ROOT_DIR + "/banner.txt", "r")
    bannerLog = bannerFile.read()
    bannerFile.close()

    bannerLog = bannerLog.replace("package.name", Config.TITLE)
    bannerLog = bannerLog.replace("package.version", Config.VERSION)
    bannerLog = bannerLog.replace("python.version", platform.python_version())
    bannerLog = bannerLog.replace("flask.version", importlib.metadata.version("flask"))
    bannerLog = bannerLog.replace("server.path", Config.SERVER_PATH)
    bannerLog = bannerLog.replace("server.port", Config.SERVER_PORT.__str__())

    print(bannerLog)

showBanner()