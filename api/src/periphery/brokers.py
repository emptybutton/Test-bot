from faststream.redis import RedisBroker

from src.periphery.envs import Env


_redis_url = f"redis://{Env.redis_host.value}:{Env.redis_port.value}"
redis_broker = RedisBroker(_redis_url)
