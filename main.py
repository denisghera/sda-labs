from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World! This is FastAPI running on Render."}

if __name__ == "__main__":
    print("Log: Starting local server...")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)