# imports
from flask import Flask, request
import json
import tensorflow as tf
app = Flask(__name__)

# getting the home.html
@app.route('/')
def getWeb():
    return app.send_static_file('home.html')

# getting the power and sending it
# request the data
# load the data using json
# get the speed
# load powerproduction from model
# get predictions
# turn it to a 1 dimensional array using flatten and return it
@app.route('/calculate/power', methods=['POST'])
def powerPrediction():
    data = request.data
    jsonLoad = json.loads(data)
    windSpeed = float(jsonLoad['speed'])
    model = tf.keras.models.load_model('powerProduction.h5')
    prediction = model.predict([windSpeed])
    flattenTo1D = prediction.flatten()
    return str(flattenTo1D[0])