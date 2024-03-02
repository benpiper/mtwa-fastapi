from fastapi import FastAPI, Path
from typing import Annotated
from controllers.serverinfo import router as ServerinfoRouter
import uvicorn
import string
import random
import socket
import time

app = FastAPI()

app.include_router(ServerinfoRouter, prefix="/serverinfo")

@app.get('/')
def home():
    return 'Hello World!'

@app.get('/random')
def get_random():
    return ''.join(random.choice(string.printable) for _ in range(6291456))

@app.get('/random/{length}')
def get_random(length: Annotated[int, Path( le=1024)]):
    return ''.join(random.choice(string.printable) for _ in range(length))

@app.get('/delay/{seconds}')
def get_delay(seconds: int):
    time.sleep(seconds)

if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=5000, reload=True)