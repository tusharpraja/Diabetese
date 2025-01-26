import json
from flask import Flask,request
from flask_cors import CORS,cross_origin
import pickle
import numpy as np


def loadModel(modelPath):
    return pickle.load(open(modelPath, 'rb'))

def validateDataType(data):
    for keys in data:
        try :
            if not isinstance(data[keys],(float,int)) :
                data[keys] =  float(data[keys])
        except:
            return (False,None)
    return (True,data)

def generateResponse(app,body,status):
    return app.response_class(response=json.dumps(body),status=status,mimetype='application/json')


app = Flask(__name__)

@app.route('/predict', methods=['POST'])    
@cross_origin()
def predict():
    if (request.headers.get('Content-Type') == 'application/json'):
        d = request.get_json()
        print(d)
        if  ( ("pregnancies"  in d) and ("glucoseLevel"  in d) and ("bloodPressure"  in d) and ("skinthickness"  in d) and
                ("insulin"  in d) and ("bmi"  in d) and ("age"  in d) and ("diaPedigreeFunc"  in d)   ):
        
            err, iD =  validateDataType(d)

            if not err:
                return generateResponse(app,{"msg":"bad payload"},400)

            input_data = (iD["pregnancies"],iD["glucoseLevel"],iD["bloodPressure"],iD["skinthickness"],iD["insulin"],iD["bmi"],iD["diaPedigreeFunc"],iD["age"])
            inputreshaped = np.asarray(input_data).reshape(1,-1)
            return  generateResponse(app,{"isDiabetic":int(model.predict(inputreshaped)[0])},200)
        return generateResponse(app,{"msg":"bad payload"},400)


    else:
        res = app.response_class(
                    response=json.dumps({"msg":"content-type not supported"}),
                        status=400,
                        mimetype='application/json'
                        )
        return res

model = loadModel('diabetes_model.sav')
app.run(debug=True,port=5000)

