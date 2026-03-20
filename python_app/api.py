from fastapi import FastAPI
from python_app.app import call_go_http, encrypt

app = FastAPI(title="Multilang System API")

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/process")
def process(numbers: list[int]):
    try:
        result = call_go_http(numbers)
        enc = encrypt()
        return {
            "go_result": result,
            "encrypted": enc
        }
    except Exception as e:
        return {"error": str(e)}