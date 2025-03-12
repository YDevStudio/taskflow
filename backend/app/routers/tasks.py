from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

from app.database import get_db
from app import models, schemas
from app.routers.auth import get_current_user

router = APIRouter()

@router.post("/", response_model=schemas.TaskOut)
def create_task(task: schemas.TaskCreate,
                db: Session = Depends(get_db),
                current_user: models.User = Depends(get_current_user)):
    new_task = models.Task(
        title=task.title,
        description=task.description,
        category=task.category,
        priority=task.priority,
        due_date=task.due_date,
        owner_id=current_user.id
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@router.get("/", response_model=List[schemas.TaskOut])
def get_tasks(db: Session = Depends(get_db),
              current_user: models.User = Depends(get_current_user)):
    tasks = db.query(models.Task).filter(models.Task.owner_id == current_user.id).all()
    return tasks

@router.get("/{task_id}", response_model=schemas.TaskOut)
def get_task(task_id: int,
             db: Session = Depends(get_db),
             current_user: models.User = Depends(get_current_user)):
    task = db.query(models.Task).filter(models.Task.id == task_id,
                                        models.Task.owner_id == current_user.id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found.")
    return task

@router.put("/{task_id}", response_model=schemas.TaskOut)
def update_task(task_id: int,
                updated_task: schemas.TaskUpdate,
                db: Session = Depends(get_db),
                current_user: models.User = Depends(get_current_user)):
    task_query = db.query(models.Task).filter(models.Task.id == task_id,
                                              models.Task.owner_id == current_user.id)
    task = task_query.first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found.")

    update_data = updated_task.dict(exclude_unset=True)  # Only include provided fields
    for field, value in update_data.items():
        setattr(task, field, value)

    db.commit()
    db.refresh(task)
    return task

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int,
                db: Session = Depends(get_db),
                current_user: models.User = Depends(get_current_user)):
    task_query = db.query(models.Task).filter(models.Task.id == task_id,
                                              models.Task.owner_id == current_user.id)
    task = task_query.first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found.")

    task_query.delete(synchronize_session=False)
    db.commit()
    return