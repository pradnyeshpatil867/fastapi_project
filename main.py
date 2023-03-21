from typing import List
from fastapi import FastAPI
from uuid import UUID, uuid4
from models import User,Gender, Role

app = FastAPI()

db : List[User] = [
    User( 
        id=uuid4(), 
        first_name="Prajakta",
        last_name="Patil",
        gender=Gender.female,
        roles=[Role.student]  
    ),
    User( 
        id=uuid4(), 
        first_name="Rohan",
        last_name="Salunkhe",
        gender=Gender.male,
        roles=[Role.admin, Role.user]  
    )
]

@app.get("/")

async def root():
    return {"Hello":"Pragya"}

@app.get("/api/v1/users")
async def fetch_users():
    return db;

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return{"id": user.id}