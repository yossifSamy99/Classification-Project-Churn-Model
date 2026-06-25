from fastapi import FastAPI,HTTPException,Depends
from fastapi.security import APIKeyHeader
from fastapi.middleware.cors import CORSMiddleware
from utils.inference import predict_new
from utils.CustomerData import CustomerData
from utils.config import APP_NAME , VERSION , SECRET_KEY_TOKEN , preprocessor , RandomForestTuned,xgb_tuned
import pandas as pd

app=FastAPI( title=APP_NAME , version=VERSION )


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/",tags=["General"])
def home():
    return{
        f"Welcom to our {APP_NAME} v {VERSION}"
    }

api_key_header=APIKeyHeader(name="X-API-Key")

async def verify_api_key(api_key:str =Depends(api_key_header)):
    if api_key!=SECRET_KEY_TOKEN:
        raise HTTPException(status_code=403,detail="You are notauthorized")
    else:
        return api_key
    


@app.post("/predict/forest",tags=["Models"])
async def predict_forest(data : CustomerData,api_key:str =Depends(api_key_header))-> dict:
    try:
        result=predict_new(data=data,preprocessor=preprocessor,model=RandomForestTuned)
        return result
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
    
@app.post("/predict/XGboost",tags=["Models"])
async def predict_XGBoost(data : CustomerData,api_key:str =Depends(api_key_header))-> dict:
    try:
        result=predict_new(data=data,preprocessor=preprocessor,model=xgb_tuned)
        return result
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
