from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class SummationRequestModel(BaseModel):
    a: int
    b: int


class SummationResponseModel(BaseModel):
    sum: int


@app.post("/api/0.1v/calculate/sum")
async def sum(request_model: SummationRequestModel) -> SummationResponseModel:
    return SummationResponseModel(sum=request_model.a + request_model.b)
