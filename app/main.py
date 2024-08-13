from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.recommendations import route as route1


app=FastAPI()

origins =[
    "*"
]

@app.get('/')
def test():
    return {"hello":"route is working fine "}

app.include_router(route1,tags=['recommend'])
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]

)