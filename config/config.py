from environs import Env
from dataclasses import dataclass

@dataclass
class TgBot:
    token: str

@dataclass
class LogSettings:
    level: str
    format: str

@dataclass
class Config:
    bot: TgBot
    log: LogSettings

def get_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        TgBot(token = env('BOT_TOKEN')),
        LogSettings(
            level = env('LEVEL'),
            format = env('LOG_FORMAT'),
        )
    )


