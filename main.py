from fastapi import FastAPI
from pydantic import BaseModel


class Steps(BaseModel):
    steps: int = None


app = FastAPI()


def statics():
    statics.fibonacci_old = 0
    statics.fibonacci_new = -1


statics.fibonacci_old = 0
statics.fibonacci_new = -1

JSON_KEY = "fibonacci"


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/fibonacci")
async def get_fibonacci():
    if statics.fibonacci_new == -1:
        return {JSON_KEY: 0}
    else:
        return {JSON_KEY: statics.fibonacci_new}


@app.post("/fibonacci")
async def calculate_steps(steps: Steps):
    if steps.steps is not None:
        for x in range(0, steps.steps):
            if statics.fibonacci_new == -1:
                statics.fibonacci_new = 1
            else:
                temp = statics.fibonacci_old + statics.fibonacci_new
                statics.fibonacci_old = statics.fibonacci_new
                statics.fibonacci_new = temp
        return {JSON_KEY: statics.fibonacci_new}

    else:
        if statics.fibonacci_new == -1:
            statics.fibonacci_new = 1
            return {JSON_KEY: statics.fibonacci_new}
        else:
            temp = statics.fibonacci_old + statics.fibonacci_new
            statics.fibonacci_old = statics.fibonacci_new
            statics.fibonacci_new = temp
            return {JSON_KEY: temp}


@app.delete("/fibonacci")
async def reset():
    statics.fibonacci_old = 0
    statics.fibonacci_new = -1
    return {"message": "Successfully reset fibonacci."}
