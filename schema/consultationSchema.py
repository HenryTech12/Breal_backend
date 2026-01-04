from pydantic import BaseModel

class ConsultationSchema(BaseModel):
    type: str
    scheduled_at: str
    project_stage: str
    site_location: str
    budget_range: str
    key_concerns: str
