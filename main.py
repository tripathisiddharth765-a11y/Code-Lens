from fastapi import FastAPI,Query,HTTPException
import json

def load_patients():
    with open("patients.json","r") as f:
        data=json.load(f)
        
    return data    

app=FastAPI()

@app.get("/")
def helo():
    return {"string":"Pateint management system"}

@app.get("/veiw")
def details(id:str):
    data=load_patients()
    for patient in data:
        if patient["id"]==id:
            return patient
        
    return {"error":"does not contain"}

@app.get("/sort")
def sort(sort_by:str=Query(...,description="Sort by ancending order")):
    value=["age","weight","bmi"]
    if sort_by not in value:
        raise HTTPException(status_code=404,detail="Wrong Request , choose from these f{value}")
    data=load_patients()
    sorted_data=sorted(data,key=lambda x:x.get(sort_by,0),reverse=False)
    
    return sorted_data