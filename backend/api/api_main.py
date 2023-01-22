from fastapi import FastAPI
from constants import API_PREFIX
from models import Budget, Aggregated

app = FastAPI()

@app.get(f"{API_PREFIX}/budget")
async def getBudget(category: str, month: int, year: int) -> Budget:
    return {"message": "Hello from Simple Budget!"}

@app.post(f"{API_PREFIX}/source")
async def createSource():
    return {"message": "Hello from Simple Budget!"}

@app.put(f"{API_PREFIX}/source")
async def updateSource():
    return {"message": "Hello from Simple Budget!"}

@app.delete(f"{API_PREFIX}/source")
async def deleteSource(category: str, month: int, source: str):
    return {"message": "Hello from Simple Budget!"}

@app.get(f"{API_PREFIX}/aggregated")
async def getAggregatedData(year: int) -> Aggregated:
    aggregatedData: Aggregated = {
        "tbd": None
    }
    return aggregatedData
