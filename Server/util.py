import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None


def calc_price(area, bhk, bathroom, furnishing, parking, status1, transaction, TYPE, locality):
    try:
        loc_index = __data_columns.index(locality.upper())
    except:
        loc_index = -1

    map_furnishing = {'Furnished': 1, 'Semi-Furnished': 0.5, 'Unfurnished': 0}
    map_status = {'Ready To Move': 1, 'Almost Ready': 0}
    map_transaction = {'New Property': 1, 'Resale': 0}
    map_type = {'Apartment': 1, 'Builder Floor': 0}
    number_of_features = len(__data_columns)
    print(number_of_features)
    x = np.zeros(number_of_features)
    x[0] = area
    x[1] = bhk
    x[2] = bathroom
    x[3] = map_furnishing[furnishing]
    x[5] = parking
    x[6] = map_status[status1]
    x[7] = map_transaction[transaction]
    x[8] = map_type[TYPE]
    if loc_index >= 0:
        x[loc_index] = 1
    log_price = __model.predict([x])[0]
    return int(np.exp(log_price))


def load_saved_artifacts():
    print("loading saved Artifacts...start")
    global __data_columns
    global __locations
    global __model

    with open("./Artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[8:]

    if __model is None:
        with open('./Artifacts/delhi_housing_price_model_new.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved Artifacts...done")


def get_location_names():
    return __locations


def get_data_columns():
    return __data_columns


if __name__ == '__main__':
    load_saved_artifacts()
    #print(get_location_names())
    price = calc_price(1540, 3, 3, 'Furnished', 1.0, 'Ready To Move', 'Resale', 'Apartment', "Uttam Nagar")
    print (price)