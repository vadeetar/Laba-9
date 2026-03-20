from fastapi import FastAPI
from python_app.app import call_go, encrypt

app = FastAPI()

@app.get("/")
def root():
    return {"status":"ok"}

@app.post("/process")
def process(numbers:list[int]):
    return {"go_result":call_go(numbers),"encrypted":encrypt()}
