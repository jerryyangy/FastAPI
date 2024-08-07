
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import post, user, auth



# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [" * "]

app.add_middleware (
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# my_post = [{"title": "title of post1", "content": "content of post 1", "id":1}, {"title": "title of post2", "content": "content of post 2", "id":2}]

# # this is the function to define how to find a post by using the post 'id'
# def find_post(id):
#     for p in my_post:
#         if p["id"] == id:
#             return p
        
# # this is the function to define how to find the post by using the post 'id' to delete the post
# def find_index_post(id):
#     for i, p in enumerate(my_post):
#         if p['id'] ==id:
#             return i

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Welcome to my API"}


