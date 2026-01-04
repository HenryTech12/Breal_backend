from model import consultationModel
from fastapi import HTTPException, status

def create_consultation(data,db):
    consultation_data = consultationModel.ConsultationModel(type=data.type,scheduled_at = data.scheduled_at, project_stage=data.project_stage, site_location=data.site_location, budget_range = data.budget_range, key_concerns=data.key_concerns, status="")
    db.add(consultation_data)
    db.commit()
    db.refresh(consultation_data)
    
    return {
        "consultation_id"
    }