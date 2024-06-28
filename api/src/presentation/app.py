from fastapi import FastAPI
from pydantic import BaseModel

from src.cases import calculating


app = FastAPI()


class SummationRequestModel(BaseModel):
    a: int
    b: int


class SummationResponseModel(BaseModel):
    sum: int


@app.post("/api/0.1v/calculate/sum")
async def sum(request_model: SummationRequestModel) -> SummationResponseModel:
    sum_ = await calculating.summate(request_model.a, request_model.b)

    return SummationResponseModel(sum=sum_)


class MultiplicationRequestModel(BaseModel):
    a: int
    b: int


class MultiplicationResponseModel(BaseModel):
    multiplication: int


@app.post("/api/0.1v/calculate/multiplication")
async def multiply(
    request_model: MultiplicationRequestModel,
) -> MultiplicationResponseModel:
    multiplication = await calculating.multiply(request_model.a, request_model.b)

    return MultiplicationResponseModel(multiplication=multiplication)
