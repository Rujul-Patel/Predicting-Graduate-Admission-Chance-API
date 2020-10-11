from flask import Flask
import os

app = Flask(__name__)

#Test Route
@app.route('/test',methods=['GET'])
def test():
    return 'Pinging Model Application!!'




#Prediction from model
import pickle
import sys
import pandas as pd
import numpy  
import matplotlib.pyplot as plt
import seaborn as sns
from flask import request,jsonify

@app.route('/predict',methods=['POST'])
def predict():

    #Reading model from binary file
    with open('model/model.bin','rb') as f_in:
        model = pickle.load(f_in)
    
    student_data = request.get_json()

    #Convert i/p to json
    data_df = pd.DataFrame(student_data,index=[0])

    res = {
            'Chance of Admission':model.predict(data_df)[0][0]
    }

    return jsonify(res)
