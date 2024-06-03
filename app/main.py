import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import router
from app.config import configuration

application: FastAPI = FastAPI(title="CRUD Application")

origins: list = [    
    "*"
]
application.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
application.include_router(router)

if __name__ == "__main__":
    uvicorn.run(
        app="main:application",
        host=configuration.get('uvicorn', 'host'),
        port=configuration.getint('uvicorn', 'port'),
        workers=configuration.getint('uvicorn', 'workers'),
        reload=configuration.getboolean('uvicorn', 'reload')
    )