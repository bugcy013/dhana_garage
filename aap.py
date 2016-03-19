__author__ = 'dhana013'

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return """<html>
                <head>
                    <title>Hello,World</title>
                </head>
                    <body>
                        <h1>Hello flask!!!</h1>
                    </body>

              </html>"""


if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')

    try:
        PORT = os.environ.get('SERVER_PORT', '5000')

    except:

        PORT = 5555

    app.run(debug='Ture')