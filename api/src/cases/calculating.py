from src.facades import mq_gateway


async def summate(a: int, b: int) -> int:
    return a + b


async def multiply(a: int, b: int) -> int:
    result = a * b

    await mq_gateway.push_multiplication_occurred(a, b, result)

    return result
