from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def root():
    return "Hello"
