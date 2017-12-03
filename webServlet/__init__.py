from __future__ import unicode_literals
from flask import Flask,jsonify,json
from flask import render_template
from flask import request
from model_function import model
import os
import base64

app = Flask(__name__) 

@app.route('/')
def firstpage():
     return render_template('index.html')
@app.route('/second')
def secondpage():
     return render_template('secondpage.html')
@app.route('/search' , methods=['GET'])
def search():
    imgsrc=request.args.get('img_src')
    code=imgsrc.split(",")
    strs=code[1].split("HTTP")
    strg=strs[0].replace(" ","+")
    strg+="===="
    imgdata=base64.b64decode(strg)
    file=open("temp.jpg","wb")
    file.write(imgdata)
    file.close()
    result=model("temp.jpg")
    response = app.response_class(
        response=result,
        status=200,
        mimetype='application/json'
    )
    return response
 #   return model(imgsrc)
@app.route('/third')
def thirdpage():
     return render_template('pagethree.html')
if __name__ == '__main__': 
 app.run()