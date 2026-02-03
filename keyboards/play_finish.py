from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from lexicon.lexicon import LEXICON

def create_play_finish_keyboard(play = True, finish = True):
    play_button = KeyboardButton(text = LEXICON['play'])
    finish_button = KeyboardButton(text = LEXICON['finish'])
    if play and not finish:
        kb = ReplyKeyboardMarkup(keyboard = [[play_button]], resize_keyboard=True)
    elif finish and not play:
        kb = ReplyKeyboardMarkup(keyboard = [[finish_button]], resize_keyboard=True)
    else:
        kb = ReplyKeyboardMarkup(keyboard = [[play_button], [finish_button]], resize_keyboard=True)
    return kb


