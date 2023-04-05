import joblib
from flask import Flask, jsonify, request
import json
import numpy as np
import sklearn


app = Flask(__name__)
model = joblib.load('/Users/aroshapunchihewa/Documents/iit/sdgp/sleepState.joblib')
def parse_json(data):
    if isinstance(data, list):
        return [parse_json(x) for x in data]
    elif isinstance(data, dict):
        return {key: parse_json(value) for key, value in data.items()}
    elif isinstance(data, str) and data.isdigit():
        return int(data)
    else:
        return data

@app.route('/predict', methods=['POST'])
def predict():
    data = json.loads(request.data.decode('utf-8'))
    nested_int_array = parse_json(data)
   # data = json.loads(request.data.decode('utf-8'))
   # int_array = [int(x) for x in data]
   # event = json.loads(request.data)
   # values = event['values']
  #  values = list(map(np.float.values))
  #  pre = np.array(values)
   # pre = pre.reshape(1, -1)
    res = model.predict(nested_int_array)
    string_array = list(map(str, res))

    print(res)
    return jsonify(string_array)


#  return str([0])


if __name__ == '__main__':
    app.run()
