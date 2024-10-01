from typing import Dict, List
import requests
import json

BASE_URL = "http://127.0.0.1:8005/"
HEADERS = {'Content-type': 'application/json'}

def search_and_list_insurance_tool(
        input: str = None,
        category_id: str = None,
        **kwargs
    ) -> Dict:
        """Search for a Insurance.
            Print the returned list of insurance.
            This function is required to be passed a category provided by user
            Returns: Insurance json list for given category, including insurance details.

        Action input:
            category_id (str): the category id for insurance

        List of category_id available:
            input "bike_insurance" for Bike insurance 
            input "car_insurance" for Car insurance
            input "health_insurance" for Health insurance 
            input "life_insurance" for Life insurance

        Structure response examples:
            { category_id : 'bike_insurance' } 
            { category_id : 'car_insurance' }
            { category_id : 'health_insurance' }
            { category_id : 'life_insurance' }
        """

        if category_id == None:
            return "You did not provide category_id : example_insurance. Try again"
        
        URL = BASE_URL + "search-insurance"

        data = {
            "category": category_id
        }
        
        response = requests.post(url=URL, data=json.dumps(data), headers=HEADERS)
        
        return { "message": "You are restricted to just use the tool_response to respond", "tool_response" : json.loads(response.content)}


def bike_insurance_claim_tool(
        input: str = None,
        policy_number: str = None,
        insured_name: str = None,
        claim_type: str = None,
        incident_details: str = None,
        policy_report_number: str = None,
        bike_make: str = None,
        bike_model: str = None,
        bike_year = None,
        **kwargs
    ) -> Dict:
    """Apply to claim bike insurance claim.
            Print the returned insurance claim status.
            This function is required to be passed the Action input provided by user
            Returns: Insurance claim status.

        Action input:
            policy_number (str) : the policy number provided by the user
            insured_name (str) : the insured name provided by the user
            claim_type (str) : the claim type provided by the user
            incident_details (str) : the incident details provided by the user
            policy_report_number (str) : the policy report number provided by the user
            bike_make (str) : the bike company provided by the user
            bike_model (str) : the bike model provided by the user
            bike_year (str) : the year bike was brought provided by the user

        Structure response examples:
            { 'policy_number' : 'example_number', 'insured_name' : 'example name', 'claim_type' : 'example type', 'incident_details' : 'example details', 'policy_report_number' : 'example number', bike_make: 'example company', 'bike_model' : 'example model' , 'bike_year' : 'example year'}
        """
    
    if policy_number is None:
        return "Ask the user to provide the policy number of the insurance"
    if insured_name is None:
        return "Ask the user to provide the insured name of the insurance"
    if claim_type is None:
        return "Ask the user to provide the claim type"
    if incident_details is None:
        return "Ask the user to provide the incident details"
    if policy_report_number is None:
        return "Ask the user to provide the policy report number of the insurance"
    if bike_make is None:
        return "Ask the user to provide company of the bike"
    if bike_model is None:
        return "Ask the user to provide model of the bike"
    if bike_year is None:
        return "Ask the user to provide purchase year of the bike"
    

    URL = BASE_URL + "bike-insurance-claim"

    data = {
        "policyNumber": policy_number,
        "insuredName": insured_name,
        "claimType": claim_type,
        "vehicleDetails": {
          "make": bike_make,
          "model": bike_model,
          "year": str(bike_year)
        },
        "incidentDetails": incident_details,
        "policeReportNumber": policy_report_number,
        "supportingDocuments": [
          {
            "doc_type": "Police Report",
            "file": "police_report.pdf"
          }
        ]
      }
    
    response = requests.post(url=URL, data=json.dumps(data), headers=HEADERS)
    response = json.loads(response.content)
    data = {
          "message": "Successfully Applied for the insurance claim", 
          "claim_number": response["message"]["claimNumber"],
    }

    return { "message": "You are restricted to just use the tool_response to respond", "tool_response" : data}


if __name__ == "__main__":
        # print(search_and_list_insurance_tool(category_id="bike_insurance"))
        print(bike_insurance_claim_tool())

