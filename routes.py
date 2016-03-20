__author__ = 'dhana013'

from flask import Flask, url_for, request, render_template
from app import *
import redis

# server/
@app.route('/')
def hello():
    # connect to redis data store
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    # alternative way connect redis
    # r = redis.StrictRedis()
    # r = redis.StrictRedis('localhost',6379,0)


    createLink = "<a href='" + url_for('create') + "'>Create a Question</a>"
    return """<html>
                <head>
                    <title>Hello,World</title>
                </head>
                    <body>
                        """ + createLink + """
                    </body>

              </html>"""


# server/create
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('CreateQuestion.html')

    elif request.method == 'POST':
        title = request.form['title']
        answer = request.form['answer']
        question = request.form['question']

        # templatefilename <parameter> <variable>
        return render_template('CreatedQuestion.html', question = question)

        # Store data in data store
    else:
        return "<h2>Invalid request</h2>"


# server/question/<title>
@app.route('/question/<title>', methods=['GET', 'POST'])
def question(title):
    if request.method  == 'GET':
        question = 'Question here'
        # read question from date store
        return render_template('AnswerQuestion.html', question=question)

    elif request.method == 'POST':
        submittedAnswer = request.form['submittedAnswer']


        # Read answer from data store

        answer = 'Answer'

        if submittedAnswer == answer:
            return  render_template('Correct.html')

        else:
            return render_template('InCorrect.html', submittedAnswer=submittedAnswer, answer=answer)
    else:
        return '<h2> Invalid request </h2>'