from flask import Flask, render_template, request
from flask import jsonify 
import requests
import pickle
import numpy as np
import sklearn 

app = Flask(__name__)
model = pickle.load(open('MODEL.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        AGE = int(request.form['AGE'])
        HEIGHT = int(request.form['HEIGHT'])
        WEIGHT = int(request.form['WEIGHT'])
        GENDER = request.form['GENDER']
        if(GENDER=='FEMALE'):
            sex = 1
        else:
            sex = 2
        AP_HIGH = int(request.form['AP_HIGH']) 
        AP_LOW = int(request.form['AP_LOW'])
        CHOLESTEROL = request.form['CHOLESTEROL']
        if(CHOLESTEROL=='NORMAL'):
            C = 1
        elif(CHOLESTEROL=='ABOVE NORMAL'):
            C = 2
        else:
            C = 3 
        GLUCOSE = request.form['GLUCOSE']
        if(GLUCOSE=='NORMAL'):
            G = 1
        elif(GLUCOSE=='ABOVE NORMAL'):
            G = 2
        else:
            G = 3
        SMOKE = request.form['SMOKE']
        if(SMOKE=='YES'):
            S = 1
        else:
            S = 0
        ALCOHOL = request.form['ALCOHOL']
        if(ALCOHOL=='YES'):
            A = 1
        else:
            A = 0
        PHYSICAL_ACTIVITY = request.form['PHYSICAL_ACTIVITY']
        if(PHYSICAL_ACTIVITY=='YES'):
            PA = 1
        else:
            PA = 0  
        
        prediction = model.predict([[AGE, HEIGHT, WEIGHT, sex, AP_HIGH, AP_LOW, C, G, S, A, PA]])
            
        
        if prediction==0:
            return render_template('index.html', prediction_text='No Risk Of Cardiovascular Disease')
            
        elif prediction ==1:
            return render_template('index.html', prediction_texts='Risk of Cardiovascular Disease')
        else:
            
            return render_template('index.html',prediction_texts="Sorry, Invalid input")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
