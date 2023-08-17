import requests
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

import numpy as np
import app.code as pdt


api_hoggen = "http://172.17.0.2:8000/api/genhog"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*']
)


@app.post("/api/carbrand")
async def genhog(request: Request):
    data = await request.json()

    try:
        hog_resp = requests.get(api_hoggen, json={"img": data['img']},headers={"Content-Type": "application/json"})
        sec_data = hog_resp.json()
        res = pdt.predict_carType(sec_data['data'])
        return {"result": res}
    except:
        raise HTTPException(status_code=500, detail="invalid value")
    

app.mount('/', StaticFiles(directory='app/web', html=True),name='static')