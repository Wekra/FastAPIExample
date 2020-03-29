from fastapi import FastAPI

app = FastAPI()

fibonacci = 1


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/fibonacci")
async def get_fibonacci():
    return {"fibonacci": fibonacci}