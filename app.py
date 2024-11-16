from fastapi import FastAPI, HTTPException
from model.model import EmployeeData  
import joblib


import uvicorn

# Load the pre-trained model
try:
   model = joblib.load('model/trained_model.pkl')
except FileNotFoundError:
    raise Exception("Model file not found. Please make sure 'trainedmodel.pkl' is in the 'model' folder.")

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Employee Salary Prediction API"}

@app.post("/predict-salary")
def predict_salary(data: EmployeeData):
    try:
        
        features = [[
           data.education_level,
           data.joining_year,
           data.city,
           data.PaymentTier,
           data.gender,
           data.EverBenched,
           data.ExperienceInCurrentDomain,
           data.LeaveOrNot

           
        ]]

        # Make prediction
        prediction = model.predict(features)
        predicted_salary = prediction[0]

        return {"predicted_salary": predicted_salary}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, port=5000, host="0.0.0.0",)
