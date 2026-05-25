from fastapi import FastAPI

import uvicorn


app = FastAPI()

@app.get('/')
async def hello():
    print('hello')
    return {"response": "hello"}
    
if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000)

