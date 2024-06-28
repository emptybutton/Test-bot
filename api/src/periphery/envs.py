from enum import Enum

import typenv


_env = typenv.Env()


class Env(Enum):
    redis_host = _env.str("REDIS_HOST")
    redis_port =_env.int("REDIS_PORT")
