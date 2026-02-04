from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/timeout-test")
async def timeout_test():
    await asyncio.sleep(800)  # start with 150, then try 300
    return {"status": "done"}
