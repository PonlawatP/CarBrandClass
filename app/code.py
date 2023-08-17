import pickle

model = pickle.load(open(f'model/carsModel.pk', 'rb'))

car_type = {
    0:"Audi",
    1:"Hyundai Creta",
    2:"Mahindra Scorpio",
    3:"Rolls Royce",
    4:"Swift",
    5:"Tata Safari",
    6:"Toyota Innova"
}

def predict_carType(HOG):
    pred = model.predict([HOG])
    return car_type[pred[0]]