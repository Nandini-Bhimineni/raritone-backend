from fastapi import FastAPI

app = FastAPI(
    title="Raritone Backend",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Raritone Backend Running"
    }