from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()

@app.get('/blog')
def index(limit,published : bool):
    if published:
        return {'data': f'{limit} published blogs from db'}
    else:
        return {'data': f'{limit} blogs from db'}

@app.get('/blog/unpublished')
def unpublished():
    return { 'data': 'all unpublished blogs'}

@app.get('/blog/{id}')
def about(id:int):
    return {"data": id}


@app.get('/blog/{id}/comments')
def comments(id):
    return {'data': {'1',2}}

class Blog(BaseModel):
    title : str
    body : str
    published : Optional[bool]


@app.post('/blog')
def create_blog(request : Blog):
    return {'data': f'Blog is created with title as {request.title}'}
