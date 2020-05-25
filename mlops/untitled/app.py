from flask import Flask,request
import pickle
import numpy as np
from flasgger import Swagger #
import pandas as pd
with open("./rf.pkl",'rb')as model_pkl:
    model=pickle.load(model_pkl)

app = Flask(__name__)
swagger=Swagger(app) #Its famous tool for auto generating API documentat ion

### Below will be requiring input in url for all 4 values
### NOTE : it's like we are giving clean UI for user to just pass value and get predictions
##they want one line example : name is value passing to api,in is input type...
@app.route('/predict')
def prediction():
    """Example endpoint returning a prediction of iris
    ---
    parameter:
      - name: s_length
        in: query
        type: number
        required: true
      - name: s_width
        in: query
        type: number
        required: true
      - name: p_length
        in: query
        type: number
        required: true
      - name: p_width
        in: query
        type: number
        required: true
    """
    s_length=request.args.get("s_length")
    s_width=request.args.get("s_width")
    p_length=request.args.get("p_length")
    p_width=request.args.get("p_width")
    predict=model.predict(np.array([[s_length,s_width,p_length,p_width]]))
    return str(predict)

### we have created a file now will use that to provide input
##to make this working we will need postman app
##but well do without  using FLASGGER
@app.route('/prediction',methods=['POST'])
def predict_file():
    """Example file endpoint returning a prediction of iris
    ---
    parameters:
      - name: data
        in: formData
        type: file
        required: true
    """
    inputdata=pd.read_csv(request.files.get("data"),header=None)
    prediction=model.predict(inputdata)
    return str(list(prediction))

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
