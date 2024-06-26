from enum import Enum

import typenv


_env = typenv.Env()


class Env(Enum):
    bot_token = _env.str("BOT_TOKEN")
    calculator_url = _env.str("CALCULATOR_URL")
