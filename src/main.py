import uvicorn

from fastapi import FastAPI



app = FastAPI()



if __name__ == '__main__':
    print('Start')
    uvicorn.run('main:app', reload=True)
    
