from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/test503")
async def test503():
    return JSONResponse(
        status_code=503,
        content={
            "code": "unavailable",
            "message": "Service Unavailable"
        },
        headers={"Retry-After": "5"}
    )
