from fastapi import FastAPI
from pydantic import BaseModel

from schema import (
    InsuranceCategory, 
    VehicaleInsurance, 
    HealthInsurance, 
    LifeInsurance
)

from utils import generate_unique_id, load_database

# Dummy Database
db = load_database()

app = FastAPI()

# Server health check Route
@app.get("/")
async def root():
    return {"message": "YO YO 🎉"}



# Search Route 
@app.post("/search-insurance/")
async def search_insurance_route(search_insurance: InsuranceCategory):
    data = db["search"][search_insurance.category]
    return { "message" : data }



# Form info Route
@app.post("/insurance-form-format/")
async def insurance_from_format_route(insurance_form: InsuranceCategory):
    data = db["form_format"][insurance_form.category]
    return { "message" : data }



# Fill Form Route
@app.post("/bike-insurance-claim/")
async def bike_insurance_route(bike_from: VehicaleInsurance):
    doc_id = generate_unique_id()
    claim_id = generate_unique_id()
    bike_from.insurance_type = "bike insurance"
    bike_from.claimNumber = claim_id
    bike_from.claimDate = "2024-09-26"
    db["claims"][doc_id] = bike_from
    return { "message" : db["claims"][doc_id]  }


@app.post("/car-insurance-claim/")
async def car_insurance_route(car_from: VehicaleInsurance):
    doc_id = generate_unique_id()
    claim_id = generate_unique_id()
    car_from.insurance_type = "car insurance"
    car_from.claimNumber = claim_id
    car_from.claimDate = "2024-09-26"
    db["claims"][doc_id] = car_from
    return { "message" : db["claims"][doc_id]  }


@app.post("/health-insurance-claim/")
async def health_insurance_route(health_from: HealthInsurance):
    doc_id = generate_unique_id()
    claim_id = generate_unique_id()
    health_from.insurance_type = "health insurance"
    health_from.claimNumber = claim_id
    health_from.claimDate = "2024-09-26"
    db["claims"][doc_id] = health_from
    return { "message" : db["claims"][doc_id] }


@app.post("/life-insurance-claim/")
async def life_insurance_route(life_from: LifeInsurance):
    doc_id = generate_unique_id()
    claim_id = generate_unique_id()
    life_from.insurance_type = "health insurance"
    life_from.claimNumber = claim_id
    life_from.claimDate = "2024-09-26"
    db["claims"][doc_id] = life_from
    return { "message" : db["claims"][doc_id] }


# Single Detail Route for Policies and Claims
