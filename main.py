from fastapi import FastAPI
from datetime import datetime
import uvicorn
import requests

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World! This is FastAPI running on Render."}

@app.get("/time")
def get_time():
    return {"current_time": datetime.now().isoformat()}

@app.get("/local-info")
def get_info():
    try:

        resp = requests.get("https://ipinfo.io/json", timeout=5)
        resp.raise_for_status()
        data = resp.json()

        return {
            "ip": data.get("ip"),
            "city": data.get("city"),
            "region": data.get("region"),
            "country": data.get("country"),
            "loc": data.get("loc"),  # "lat,long"
            "org": data.get("org"),
            "raw": data
        }
    except Exception as e:
        return {"error": "Could not determine location", "details": str(e)}

if __name__ == "__main__":
    print("Log: Starting local server...")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)