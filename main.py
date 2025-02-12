from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

app = FastAPI()

class ModelInput(BaseModel):  # Class names should follow PascalCase
    Text: str  # Variable names should follow snake_case (optional)

# Load the saved model
model = pickle.load(open("spam_model.sav", 'rb'))

@app.post("/spam_prediction")
def spam_prediction(input_parameters: ModelInput):
    input_data = input_parameters.json() 
    input_dictionary = json.loads(input_data) 
    text = input_dictionary["Text"]  

    
    prediction = model.predict([text])[0] 

    return {"prediction": "spam" if prediction == 1 else "ham"}
