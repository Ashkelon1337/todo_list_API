from models import Todolist, TaskCreate, TaskResponse
from database import init_db, get_session
from typing import Annotated
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import FastAPI, Depends, HTTPException
import uvicorn

app = FastAPI()

SessionDep = Annotated[AsyncSession, Depends(get_session)]

@app.on_event('startup')
async def create_db():
    await init_db()
    print('database created!!')

@app.post('/tasks', response_model=TaskResponse)
async def create_task(todolist: TaskCreate, session: SessionDep):
    task = Todolist(title=todolist.title)
    session.add(task)
    await session.commit()
    await session.refresh(task)
    return task

@app.get('/tasks', response_model=list[TaskResponse])
async def get_tasks(session: SessionDep):
    data = await session.scalars(select(Todolist))
    return data.all()
@app.get('/tasks/{task_id}', response_model=TaskResponse)
async def get_task(task_id: int, session: SessionDep):
    data = await session.scalar(select(Todolist).where(Todolist.id == task_id))
    if not data:
        raise HTTPException(status_code=404, detail='Задание не найдено!')
    return data
@app.put('/tasks/{task_id}', response_model=TaskResponse)
async def swap_completed(task_id: int, session: SessionDep):
    data = await session.scalar(select(Todolist).where(Todolist.id == task_id))
    if not data:
        raise HTTPException(status_code=404, detail='Задание не найдено!')
    data.completed = not data.completed
    await session.commit()
    await session.refresh(data)
    return data

@app.delete('/tasks/{task_id}')
async def delete_task(task_id: int, session: SessionDep):
    data = await session.scalar(select(Todolist).where(Todolist.id == task_id))
    if not data:
        raise HTTPException(status_code=404, detail='Задание не найдено!')
    await session.delete(data)
    await session.commit()
    return {'ok': True, 'message': f'Задание {task_id} успешно удалено!'}
if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)