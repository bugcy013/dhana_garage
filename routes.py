__author__ = 'dhana013'

from flask import Flask, url_for, request, render_template
from app import *
import redis

# connect to redis data store
r = redis.StrictRedis(host='localhost', port=6379, db=0, charset='utf-8', decode_responses=True)
# alternative way connect redis
# r = redis.StrictRedis()
# r = redis.StrictRedis('localhost',6379,0)

# server/
@app.route('/')
def hello():

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

        # Store data in data store
        # key name will be whatever title they typed in : Question
        # e.g. music:question countries:question
        # e.g. music:answer countries:answer
        # templatefilename <parameter> <variable>

        r.set(title +':question', question)
        r.set(title +':answer', answer)

        return render_template('CreatedQuestion.html', question=question)

    else:
        return "<h2>Invalid request</h2>"


# server/question/<title>
@app.route('/question/<title>', methods=['GET', 'POST'])
def question(title):
    if request.method  == 'GET':
        # read question from date store
        question = r.get(title+':question')
        return render_template('AnswerQuestion.html', question=question)

    elif request.method == 'POST':
        submittedAnswer = request.form['submittedAnswer']
        # Read answer from data store
        answer = r.get(title+':answer')

        if submittedAnswer == answer:
            return render_template('Correct.html')

        else:
            return render_template('InCorrect.html', submittedAnswer=submittedAnswer, answer=answer)
    else:
        return '<h2> Invalid request </h2>'