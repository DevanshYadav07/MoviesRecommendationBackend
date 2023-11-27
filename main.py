from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.recommendations import route as route1



app=FastAPI()




origins =[
    "http://localhost",
    "http://localhost:3000",
    "*"
]

@app.get('/')
def test():
    return 'route is working fine'
app.include_router(route1,tags=['recommend'])
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]

)