from fastapi import APIRouter, status, Depends
from repository import database
from schema import milestoneSchema
from sqlalchemy.orm import Session
from service import milestoneService


milestone_router = APIRouter()

@milestone_router.post('/projects/{project_id}/milestones')
def create_milestone(project_id, data: milestoneSchema.MilestoneSchema, db: Session = Depends(database.get_db)):
    return milestoneService.create_milestone(data,db,project_id)

@milestone_router.get('/projects/{project_id}/timeline')
def get_timelines(project_id, db: Session =Depends(database.get_db)):
    return milestoneService.get_timeline(project_id,db)

@milestone_router.patch('/milestones/{milestone_id}')
def update_milestone(milestone_id, my_status: str, db: Session = Depends(database.get_db)):
    data = {
        "status": my_status
    }
    return milestoneService.update_milestone(milestone_id,db,data)

@milestone_router.delete('/milestones/{milestone_id}')
def delete_milestone(milestone_id, db: Session = Depends(database.get_db)):
    return milestoneService.delete_milestone(milestone_id,db)

