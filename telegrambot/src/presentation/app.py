from aiogram import Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

from presentation.parsers import number_pair_from
from services import calculating


dispatcher = Dispatcher()


@dispatcher.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer("Привет! Напиши два числа через пробел чтобы суммировать их")


@dispatcher.message()
async def calculate(message: Message) -> None:
    number_pair = number_pair_from(message.text)

    if number_pair is None:
        await message.answer("У вас числа неправильные")
        return

    sum_ = await calculating.sumOf(*number_pair)

    if sum_ is None:
        await message.answer("Вы суммировали числа!")
        return

    await message.answer(f"Сумма — {sum_}")
