from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class GymInput(BaseModel):
    action: str

@app.get("/")
def read_root():
    return {"msg": "Gym API is up!"}

@app.post("/step")
def step(input: GymInput):
    # Integrate with your gym logic here
    return {"action_received": input.action}
