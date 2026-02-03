import asyncio
import logging
from aiogram import Bot, Dispatcher
from config.config import get_config, Config

from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from handlers.other import other_router
from handlers.user import user_router

from database.database import init_db
from keyboards.menu_commands import set_menu_commands

logger = logging.getLogger(__name__)

async def main():

    config: Config = get_config()

    logging.basicConfig(
        level = logging.getLevelName(config.log.level),
        format = config.log.format
    )

    logger.info('Starting bot')

    bot = Bot(
        token = config.bot.token,
        default = DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp: dict = Dispatcher()

    db = init_db()

    dp.workflow_data.update(db = db, main_bot = bot)

    logger.info('Назначение комманд')
    await set_menu_commands(bot)
    logger.info('Комманды назначены')

    dp.include_router(user_router)
    dp.include_router(other_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())