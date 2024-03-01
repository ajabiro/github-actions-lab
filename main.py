from fastapi import FastAPI
from pydantic import BaseModel


class Facts(BaseModel):
    id: int
    fact: str


app = FastAPI()

facts_db = [Facts(id=0, fact="Lion roars are the loudest of any other big cat"),
            Facts(id=1, fact="The Eiffel Tower can be 15 cm taller during the summer"),
            Facts(id=2, fact="Avocados are a fruit, not a vegetable"),
            Facts(id=3, fact="A crocodile cannot stick its tongue out"),
            Facts(id=4, fact="You can't hum when you hold your nose")]


@app.get('/fact')
async def get_all():
    return facts_db


@app.get('/fact/{id}')
async def get_by_id(id: int):
    return facts_db[id]


@app.post('/fact')
async def add(fact: str):
    new_fact = Facts(id=len(fact), fact=fact)
    facts_db.append(new_fact)
    return new_fact
