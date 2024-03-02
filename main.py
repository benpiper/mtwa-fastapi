"""main.py"""
import string
import random
import time
from typing import Annotated
import uvicorn
from fastapi import FastAPI, Path, HTTPException
from controllers.serverinfo import router as ServerinfoRouter

app = FastAPI()

app.include_router(ServerinfoRouter, prefix="/serverinfo")


@app.get('/')
def home():
    """Hello world"""
    raise HTTPException(status_code=404, detail="Nothing here")



@app.get('/random')
def get_random():
    """Generates a string of random characters"""
    return ''.join(random.choice(string.printable) for _ in range(6291456))


@app.get('/random/{length}')
def get_random_length(length: Annotated[int, Path(le=1024)]):
    """Generates a string of random characters of length"""
    return ''.join(random.choice(string.printable) for _ in range(length))


@app.get('/delay/{seconds}')
def get_delay(seconds: int):
    """Delay for seconds"""
    time.sleep(seconds)
    return {"message": f"Wait of {seconds} complete"}


if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=5000, reload=True)
