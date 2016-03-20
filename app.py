__author__ = 'dhana013'

from flask import Flask
app = Flask(__name__)


# import all of routes from routes.py
from routes import *



if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')

    try:
        PORT = os.environ.get('SERVER_PORT', '5000')

    except:

        PORT = 5555

    app.run(debug='Ture')