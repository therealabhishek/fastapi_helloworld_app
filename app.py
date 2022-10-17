import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return "Hello Boys!!!"

if __name__ == "__main__":
    uvicorn.run("app:app", port=8000, reload = True)
