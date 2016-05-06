'''
@author:
'''

from bottle import Bottle, template, debug, static_file
import interface
import users
from database import COMP249Db


COOKIE_NAME = 'sessionid'

application = Bottle()

@application.route('/')
def index():

    return template('index', title="Hello!")

@application.route('/static/:fileName#.*#')
def server_static(fileName):
    return static_file(fileName, root='./static')


if __name__ == '__main__':
    debug()
    application.run()
