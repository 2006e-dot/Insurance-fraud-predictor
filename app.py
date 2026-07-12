from fastapi import FastAPI, HTTPException
from typing import Literal, List
import pickle
import pandas as pd
from pydantic import BaseModel

with open('insurance_fraud_xgb.pkl','rb') as f:
    model=pickle.load(f)

with open("cols.pkl", "rb") as f:
    feature_columns = pickle.load(f)

app=FastAPI()
class User(BaseModel):
    Month: str
    WeekOfMonth: int
    DayOfWeek: str
    Make: str
    AccidentArea: str
    DayOfWeekClaimed: str
    MonthClaimed: str
    WeekOfMonthClaimed: int
    Sex: str
    MaritalStatus: str
    Age: int
    Fault: str
    PolicyType: str
    VehicleCategory: str
    VehiclePrice: str
    RepNumber: int
    Deductible: int
    DriverRating: int
    Days_Policy_Accident: str
    Days_Policy_Claim: str
    PastNumberOfClaims: str
    AgeOfVehicle: str
    AgeOfPolicyHolder: str
    PoliceReportFiled: str
    WitnessPresent: str
    AgentType: str
    NumberOfSuppliments: str
    AddressChange_Claim: str
    NumberOfCars: str
    Year: int
    BasePolicy: str

@app.post("/predict")
def predict(user:User):
    try:
        df=pd.DataFrame([user.model_dump()])
        df=pd.get_dummies(df)
        df=df.reindex(columns=feature_columns,fill_value=0)
        prediction=model.predict(df)[0]
        prob=model.predict_proba(df)[0][1]
        return {
            "prediction": "Fraud" if prediction == 1 else "Not Fraud",
            "fraud_probability": round(float(prob), 4)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/predict_batch")
def predict_batch(users:List[User]):
    try:
        df=pd.DataFrame([u.model_dump() for u in users])
        df=pd.get_dummies(df)
        df=df.reindex(columns=feature_columns,fill_value=0)
        predictions=model.predict(df)
        probs=model.predict_proba(df)[:,1]
        results=[]
        for p, pr in zip(predictions, probs):
            results.append({
                "prediction": "Fraud" if p == 1 else "Not Fraud",
                "fraud_probability": round(float(pr), 4)
            })
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))