from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from .database import name_databases
from .models import MakrovModel
import sqlite3

#schemas

class NameResponse(BaseModel):
    names : list


#app
app = FastAPI()
app.frontend("/", directory="../Frontend")


@app.get("/api/db")
def get_db_names():
    return name_databases

@app.get("/api/gen")
def get_generated_names(db_name : str, amount : int):
    nameModel = MakrovModel(db_name, 4)
    return nameModel.getNameList(amount)