from pydantic import BaseModel
from typing import List

class InsuranceCategory(BaseModel):
    category    : str

class VechicleDetails(BaseModel):
    make        : str
    model       : str
    year        : str

class SupportingDocuments(BaseModel):
    doc_type   : str
    file       : str

class TreatmentDetails(BaseModel):
    date        : str
    procedure   : str
    cost        : str


class VehicaleInsurance(BaseModel):
    insurance_type          : str | None = None
    claimNumber             : str | None = None
    claimDate               : str | None = None
    policyNumber            : str
    insuredName             : str
    claimType               : str
    vehicleDetails             : VechicleDetails
    incidentDetails         : str
    policeReportNumber      : str
    supportingDocuments     : List[SupportingDocuments] = []


class HealthInsurance(BaseModel):
    insurance_type          : str | None = None
    claimNumber             : str | None = None
    claimDate               : str | None = None
    policyNumber            : str
    insuredName             : str
    claimType               : str
    providerName            : str
    providerAddress         : str
    diagnosis               : str
    treatmentDetails        : List[TreatmentDetails] = []
    supportingDocuments     : List[SupportingDocuments] = []


class LifeInsurance(BaseModel):
    insurance_type          : str | None = None
    claimNumber             : str | None = None
    claimDate               : str | None = None
    policyNumber            : str
    insuredName             : str
    claimType               : str
    deathCertificate        : str
    beneficiaryName         : str
    supportingDocuments     : List[SupportingDocuments] = []