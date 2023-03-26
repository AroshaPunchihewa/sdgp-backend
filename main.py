import joblib
from flask import Flask, jsonify, request
import json
import numpy as np
import sklearn


app = Flask(__name__)
model = joblib.load('/Users/aroshapunchihewa/Documents/iit/sdgp/sleepState.joblib')


@app.route('/predict', methods=['POST'])
def predict():
    event = json.loads(request.data)
    values = event['values']
    values = list(map(np.float.values))
    pre = np.array(values)
    pre = pre.reshape(1, -1)
    res = model.predict(pre)
    print(res)
    return str([0])


if __name__ == '__main__':
    app.run()
