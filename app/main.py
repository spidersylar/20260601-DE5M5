from fastapi import FastAPI
from library_pipeline import run_all

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.post("/run-library-etl")
def run_etl():
    try:
        result = run_all()
        return result 
    except Exception as e:
        return {"status": "error", "message": str(e)}