from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from src.periphery.envs import Env


_properties = DefaultBotProperties(parse_mode=ParseMode.HTML)

bot = Bot(token="7283006164:AAGqziYkgHOcysW_5GtoR_1jfFb0gtP_bzI", default=_properties)
