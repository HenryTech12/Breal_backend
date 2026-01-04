from fastapi import APIRouter, Depends, database, status
from schema import contractorSchema
from service import contractorService
from sqlalchemy.orm import Session
from repository import database
from fastapi.security import HTTPAuthorizationCredentials
contractor_router = APIRouter()

@contractor_router.post('/kyc/nin/verify', status_code=status.HTTP_201_CREATED)
def create_contractor(data: contractorSchema.ContractorSchema):
    contractorService.verifyContractor(data)
    
@contractor_router.post('/contractors/profile')
def create_contractor_profile(data: contractorSchema.ContractorProfileSchema, email: str = Depends(HTTPAuthorizationCredentials), db: Session = Depends(database.get_db)):
    return contractorService.create_contractor_profile(data,email,db)

@contractor_router.get('/contractors/profile')
def fetch_contractor_profile(email: str = Depends(HTTPAuthorizationCredentials), db: Session = Depends(database.get_db)):
    return contractorService.get_contractor_profile(email,db)

@contractor_router.patch('/contractors/profile')
def update_contractor_profile(data: contractorSchema.UpdateContractorProfile, email: str = Depends(HTTPAuthorizationCredentials), db: Session = Depends(database.get_db)):
    return contractorService.update_contractor_profile(email,data,db)