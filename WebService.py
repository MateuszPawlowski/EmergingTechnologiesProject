# imports
from flask import Flask, jsonify, request
import json
import tensorflow as tf
app = Flask(__name__)

# getting the home.html 
@app.route('/')
def getWeb():
    return app.send_static_file('home.html')

# getting the power and sending it
@app.route('/calculate/power', methods=['POST'])
def powerPrediction():
    # request the data
    data = request.data
    # load the data using json
    jsonLoad = json.loads(data)
    # get the speed
    windSpeed = float(jsonLoad['speed'])
    # load powerproduction from model
    model = tf.keras.models.load_model('powerProduction.h5')
    # get predictions
    prediction = model.predict([windSpeed])
    # turn it to a 1 dimensional array using flatten and return it
    flatten = prediction.flatten()
    print(flatten[0])
    return str(flatten[0])