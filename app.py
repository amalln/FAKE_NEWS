from flask import Flask, render_template,redirect,url_for,request
import prediction

import prediction
app = Flask(__name__)

@app.route('/')
def showform():
    return render_template('index.html')



@app.route('/process',methods=['Post'])
def index():
    news= request.form['news']

    val,color=prediction.manuel_testing(news)
    return render_template('index.html',val=val,color=color)

if __name__ == '__main__':
    app.run(debug=True)
