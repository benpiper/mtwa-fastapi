from fastapi import FastAPI
from controllers.serverinfo import router as ServerinfoRouter
import uvicorn

app = FastAPI()

app.include_router(ServerinfoRouter, prefix="/serverinfo")

@app.get('/')
def home():
    return 'Hello World!'

if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=5000, reload=True)