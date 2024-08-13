from fastapi import  APIRouter
from app.routes.recommendation_system import similar_movies
route = APIRouter(prefix='/recommend')


@route.get(path='/movies',status_code=200)
def  function(input:str):
    # print('the movie you are searching is: ',input)
    suggestion_array=similar_movies(input)

    # return list to the user
    return suggestion_array
