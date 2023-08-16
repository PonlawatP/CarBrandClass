import re
import pickle
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

import numpy as np

car_type = {
    0:"Audi",
    1:"Hyundai Creta",
    2:"Mahindra Scorpio",
    3:"Rolls Royce",
    4:"Swift",
    5:"Tata Safari",
    6:"Toyota Innova"
}

model = pickle.load(open(f'model/carsPred.pk', 'rb'))

def predict_carType(mdl, HOG):
    pred = mdl.predict([HOG])
    return car_type[pred[0]]

# predict_carType(model, hg)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*']
)

# @app.get("/")
# async def root():
#     return {"message": "hello"}


@app.get("/api/carbrand")
async def genhog(request: Request):
    data = await request.json()
    try:
        res = predict_carType(model, data['hog'])
        return {"result": res}
    except:
        raise HTTPException(status_code=500, detail="invalid value")
    

app.mount('/', StaticFiles(directory='app/web', html=True),name='static')