from fastapi import FastAPI
from typing import Union
import random

app = FastAPI()

@app.get('/')
def read_root():
    return { 'greeting': 'hello world' }

@app.get('/items/{item_id}')
def read_item(item_id:int, q:Union[str, None] = None):
    return { 'item_id': item_id, 'q': q}

@app.get('/random')
def read_users(n:Union[int, None] = None):
    if n == None:
        response = { '0' : random.random() }
    else:
        response = { key:random.random() for key in range(n) }
    return response
