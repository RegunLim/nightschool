from flask import Flask, render_template, request, jsonify
from bs4 import BeautifulSoup
from pymongo import MongoClient


app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.dbtest

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/written-homework')
def writtenhomework():
    return render_template('writtenHW.html')

@app.route('/dictation-homework')
def dictationhomework():
    return render_template('dictationHW.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/lesson1')
def question():
    all_questions = list(db.lesson.find({},{'_id':0}))
    return jsonify({'result': 'success', 'lesson':all_questions})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
