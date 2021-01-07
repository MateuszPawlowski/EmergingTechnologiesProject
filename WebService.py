from flask import Flask, jsonify, request
import json
import tensorflow as tf
app = Flask(__name__)

@app.route('/')
def getWeb():
    return app.send_static_file('home.html')

@app.route('/calculate/power', methods=['POST'])
def powerPrediction():
    data = request.data
    jsonLoad = json.loads(data)
    windSpeed = float(jsonLoad['speed'])
    model = tf.keras.models.load_model('powerProduction.h5')
    prediction = model.predict([windSpeed])
    flatten = prediction.flatten()
    print(flatten[0])
    return str(flatten[0])