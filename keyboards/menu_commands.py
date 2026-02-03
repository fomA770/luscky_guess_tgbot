from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats
from aiogram import Bot
from lexicon.lexicon import LEXICON_COMS_DESC

async def set_menu_commands(bot: Bot):
    menu_commands = [
        BotCommand(
            command = command, 
            description=description
        ) for command, description in LEXICON_COMS_DESC.items()
    ]

    await bot.set_my_commands(menu_commands)