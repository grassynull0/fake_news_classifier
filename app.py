import numpy as np
from flask import Flask, request,render_template
import pickle
import flask
import newspaper
from newspaper import Article
from sklearn.feature_extraction.text import TfidfVectorizer
import urllib

import os

app = Flask(__name__)
app=flask.Flask(__name__,template_folder='html_template')


file_name = 'model1_final.pkl'

with open(file_name, 'rb') as the_model:
    model4 = pickle.load(the_model)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/predict',methods=['GET', 'POST'])
def predict():
    url = request.get_data(as_text=True)[5:]
    url = urllib.parse.unquote(url)
    article = Article(str(url))
    article.download()
    article.parse()
    article.nlp()
    news = article.summary
    pred = model4.predict([news])
    if pred[0] == 1:
        response = 'Fake'
    else:
        response = 'Real'
    return render_template('main.html', prediction_text=f'The news is "{response}"')
    
if __name__=="__main__":
    port=int(os.environ.get('PORT',5000))
    app.run(port=port,debug=True,use_reloader=False)
