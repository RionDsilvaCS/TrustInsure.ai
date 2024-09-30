import requests
import json
from typing import Dict

BASE_URL = "http://127.0.0.1:8000/"
HEADERS = {'Content-type': 'application/json'}


def search_insurance(
    category: str = "bike_insurance"
    ) -> Dict:

    URL = BASE_URL + "search-insurance"

    data = {
        "category": category
    }
    
    response = requests.post(url=URL, data=json.dumps(data), headers=HEADERS)
    
    return json.loads(response.content)

def test_search_insurance():
    insurance_list = ["bike_insurance", "car_insurance", "health_insurance", "life_insurance"]
    for category in insurance_list:
        print(category, " => ", search_insurance(category=category), end="\n\n")


def insurance_form_format(
    category: str = "bike_insurance"
    ) -> Dict:

    URL = BASE_URL + "insurance-form-format"

    data = {
        "category": category
    }
    
    response = requests.post(url=URL, data=json.dumps(data), headers=HEADERS)
    
    return json.loads(response.content)

def test_insurance_form_format():
    insurance_list = ["bike_insurance", "car_insurance", "health_insurance", "life_insurance"]
    for category in insurance_list:
        print(category, " => ", insurance_form_format(category=category), end="\n\n")


def bike_insurance_claim() -> Dict:

    URL = BASE_URL + "bike-insurance-claim"

    data = {
        "policyNumber": "BI67890",
        "insuredName": "Jane Smith",
        "claimDate": "2024-09-26",
        "claimType": "Theft",
        "vehicleDetails": {
          "make": "Honda",
          "model": "CBR1000RR",
          "year": "2023"
        },
        "incidentDetails": "Bike stolen from driveway on 2024-09-25",
        "policeReportNumber": "PR12345",
        "supportingDocuments": [
          {
            "doc_type": "Police Report",
            "file": "police_report.pdf"
          }
        ]
      }
    
    response = requests.post(url=URL, data=json.dumps(data), headers=HEADERS)
    
    return json.loads(response.content)

def car_insurance_claim() -> Dict:

    URL = BASE_URL + "car-insurance-claim"

    data = {
        "policyNumber": "CI67890",
        "insuredName": "David Lee",
        "claimType": "Collision",
        "vehicleDetails": {
          "make": "Toyota",
          "model": "Camry",
          "year": "2023"
        },
        "incidentDetails": "Car involved in a collision on 2024-09-25",
        "policeReportNumber": "PR12345",
        "supportingDocuments": [
          {
            "doc_type": "Police Report",
            "file": "police_report.pdf"
          },
          {
            "doc_type": "Repair Estimates",
            "file": "repair_estimates.pdf"
          }
        ]
      }
    
    response = requests.post(url=URL, data=json.dumps(data), headers=HEADERS)
    
    return json.loads(response.content)

def health_insurance_claim() -> Dict:

    URL = BASE_URL + "health-insurance-claim"

    data = {
        "policyNumber": "HI67890",
        "insuredName": "John Doe",
        "claimType": "Hospitalization",
        "providerName": "ABC Hospital",
        "providerAddress": "123 Main Street, Anytown, USA",
        "diagnosis": "Pneumonia",
        "treatmentDetails": [
          {
            "date": "2024-09-25",
            "procedure": "X-ray",
            "cost": "100"
          },
          {
            "date": "2024-09-26",
            "procedure": "Medication",
            "cost": "50"
          }
        ],
        "supportingDocuments": [
          {
            "doc_type": "Doctor's Note",
            "file": "doctors_note.pdf"
          },
          {
            "doc_type": "Hospital Bills",
            "file": "hospital_bills.pdf"
          }
        ]
      }
    
    response = requests.post(url=URL, data=json.dumps(data), headers=HEADERS)
    
    return json.loads(response.content)

def life_insurance_claim() -> Dict:

    URL = BASE_URL + "life-insurance-claim"

    data = {
        "policyNumber": "LI67890",
        "insuredName": "Emily Brown",
        "claimType": "Death",
        "deathCertificate": "DC12345",
        "beneficiaryName": "Michael Johnson",
        "supportingDocuments": [
          {
            "doc_type": "Death Certificate",
            "file": "death_certificate.pdf"
          }
        ]
      }
    
    response = requests.post(url=URL, data=json.dumps(data), headers=HEADERS)
    
    return json.loads(response.content)

def test_insurance_claims():

    print("bike_insurance => ", bike_insurance_claim(), end="\n\n")
    print("car_insurance => ", car_insurance_claim(), end="\n\n")
    print("health_insurance => ", health_insurance_claim(), end="\n\n")
    print("life_insurance => ", life_insurance_claim(), end="\n\n")


if __name__ == "__main__":
    print("-:-:- Search Route Test -:-:-\n")
    test_search_insurance()

    print("-:-:- Form Format Route Test -:-:-\n")
    test_insurance_form_format()

    print("-:-:- Claim Routes Test -:-:-\n")
    test_insurance_claims()
