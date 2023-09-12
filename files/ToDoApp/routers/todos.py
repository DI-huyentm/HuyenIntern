from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Path
from models import ToDos
from database import SessionLocal 
from .auth import get_current_user
from starlette import status


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db  # from this above, executed before the response
    finally:   # executed after the response
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

class ToDoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    priority: int = Field(gt=0, lt=6)
    complete: bool

@router.get("/", status_code=status.HTTP_200_OK)
async def read_all(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    return db.query(ToDos).filter(ToDos.owner_id == user.get('id')).all()

@router.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def read_todo(user: user_dependency, db: db_dependency, todo_id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    
    todo_model = db.query(ToDos).filter(ToDos.id == todo_id)\
        .filter(ToDos.owner_id==user.get('id')).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404, detail='Todo not found.')

@router.post('/todo', status_code=status.HTTP_201_CREATED)
async def create_todo(user: user_dependency, db: db_dependency, todo_request: ToDoRequest):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    todo_model = ToDos(**todo_request.model_dump(), owner_id=user.get('id'))

    db.add(todo_model)
    db.commit()

@router.put('/todo/{todo_id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(user: user_dependency, db: db_dependency, todo_request: ToDoRequest, todo_id:int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    todo_model = db.query(ToDos).filter(ToDos.id == todo_id).filter(ToDos.owner_id==user.get('id')).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail='Todo not found.')
    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.priority = todo_request.priority
    todo_model.complete = todo_request.complete

    db.add(todo_model)
    db.commit()

@router.delete('/todo/{todo_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(user: user_dependency, db: db_dependency, todo_id:int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    todo_model = db.query(ToDos).filter(ToDos.id == todo_id).filter(ToDos.owner_id==user.get('id')).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail='Todo not found.')
    db.query(ToDos).filter(ToDos.id == todo_id).filter(ToDos.owner_id==user.get('id')).delete()

    db.commit()