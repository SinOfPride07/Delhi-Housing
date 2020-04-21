from flask import Flask, request, jsonify
import util

from Server.util import calc_price

app = Flask(__name__)


@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    area = float(request.form['area'])
    locality = request.form['locality']
    bhk = int(request.form['bhk'])
    bathroom = int(request.form['bathroom'])
    furnishing = request.form['furnishing']
    parking = int(request.form['parking'])
    status1 = request.form['status1']
    transaction = request.form['transaction']
    TYPE = request.form['TYPE']
    #print(area, bhk, bathroom, furnishing, parking, status1, transaction, TYPE, locality)
    response = jsonify({
        'calc_price': util.calc_price(area, bhk, bathroom, furnishing, parking, status1, transaction, TYPE, locality)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()
