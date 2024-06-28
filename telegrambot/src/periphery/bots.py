from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from src.periphery.envs import Env


_properties = DefaultBotProperties(parse_mode=ParseMode.HTML)

bot = Bot(token=Env.bot_token.value, default=_properties)
