from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon import LEXICON
from keyboards.play_finish import create_play_finish_keyboard

other_router = Router()

@other_router.message()
async def handle_other_messages(message: Message):
    await message.answer(
        LEXICON['cant_handle_update'],
        reply_markup = create_play_finish_keyboard(finish = False)
    )
