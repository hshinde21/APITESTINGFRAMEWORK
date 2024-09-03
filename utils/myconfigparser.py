import configparser
from pathlib import Path

cfgFile = 'qa.ini'
cfgFileDir = 'config'

config = configparser.ConfigParser(allow_no_value=True)
BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)
CONFIG_FILE = BASE_DIR.joinpath(cfgFileDir).joinpath(cfgFile)
config.read(CONFIG_FILE)


def getPetAPIURL():
    return config['pet']['url']


def getFlaskAppBaseURL():
    baseURL = 'http://' + config['flaskapp']['url'] + ":" + config['flaskapp']['port'] + '/api'
    return baseURL


print(getFlaskAppBaseURL())
