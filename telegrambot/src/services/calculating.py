from typing import Optional

from infrastructure import calculator_gateway


async def sumOf(a: int, b: int) -> Optional[int]:
    return await calculator_gateway.calculate(a, b)
