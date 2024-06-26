import asyncio
import logging
import sys

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from envs import Env
from presentation.app import dispatcher


async def main() -> None:
    properties = DefaultBotProperties(parse_mode=ParseMode.HTML)
    bot = Bot(token=Env.bot_token.value, default=properties)

    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
