from common.get_cookie import *


config = configparser.ConfigParser()
config.read('../config/config.ini')

# 将get_cookie.py获得的Cookie值传入config.ini
Cookie = str(Cookie)
config['default']['Cookie'] = Cookie
with open('config.ini', 'w') as configfile:
    config.write(configfile)
