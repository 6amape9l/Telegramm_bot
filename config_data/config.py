from __future__ import annotations
from dataclasses import dataclass
from environs import Env


@dataclass
class DatabaseConfig:
    database: str  # Название базы данных
    db_host: str  # URL-адрес базы данных
    db_user: str  # Username пользователя базы данных
    db_password: str  # Пароль к базе данных


@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту
    skip_updates: bool
    admin_ids: list[int]  # Список id администраторов бота
    prem_ids: list[int]  # Список id платных подписчиков
    reply_id: int


@dataclass
class Config:
    tg_bot: TgBot


@dataclass
class User:
    lesson: int
    prem: bool


def load_config(path: str | None = None) -> Config:
    env: Env = Env()
    env.read_env(path)
    f = open("database/prems.txt", "r")

    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN'),
            skip_updates=env('SKIP_UPDATES'),
            reply_id=env('SKIP_UPDATES'),
            admin_ids=list(map(int, env.list('ADMIN_IDS'))),
            prem_ids=list(map(int, f.readline().split(','))),
        )
    )
