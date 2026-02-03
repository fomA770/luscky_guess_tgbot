from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
#from aiogram.utils.keyboard import InlineKeyboardBuilder
import random
from lexicon.lexicon import LEXICON

def _bombs_coordinates(n: int) -> list[tuple]:
    num_of_bombs = {
        4: 3,
        5: 5,
        6: 8,
    }
    bombs_coordinates = []
    while len(bombs_coordinates) != num_of_bombs[n]:
        coordinates = (random.randint(0, n-1), random.randint(0, n-1))
        if not coordinates in bombs_coordinates:
            bombs_coordinates.append(coordinates)
    return bombs_coordinates
        


def create_game_board(side: int):
    keyboard = []
    bombs = _bombs_coordinates(side)
    for i in range(side):
        row = []
        for j in range(side):
            if (i, j) in bombs:
                row.append(InlineKeyboardButton(
                    text = LEXICON['standard_button'],
                    callback_data=f'bomb.{i}.{j}.{side}'
                ))
            else:
                row.append(InlineKeyboardButton(
                    text = LEXICON['standard_button'],
                    callback_data=f'ok.{i}.{j}.{side}'
                ))
        keyboard.append(row)
    keyboard.append(
        [InlineKeyboardButton(
            text = 'Получить деньги🚀',
            callback_data='take_money',
        )]
    )
    return keyboard

def appoint_board_keyboard():
    return ReplyKeyboardMarkup(
        keyboard = [
            [KeyboardButton(text='4')],
            [KeyboardButton(text='5')],
            [KeyboardButton(text='6')],
        ],
        resize_keyboard=True
    )

def get_new_button(text) -> InlineKeyboardButton:
    return InlineKeyboardButton(
        text = text,
        callback_data = 'used'
    )


def change_to_nonactive_keyboard(keyboard: list):
    for i in range(len(keyboard) - 1):
        for j in range(len(keyboard[0])):
            if keyboard[i][j].callback_data.startswith('ok'):
                keyboard[i][j] = InlineKeyboardButton(
                    text = LEXICON['ok_button'],
                    callback_data='used'
                )
            elif keyboard[i][j].callback_data.startswith('bomb'):
                keyboard[i][j] = InlineKeyboardButton(
                    text = LEXICON['bomb_button'],
                    callback_data='used'
                )
    keyboard.pop(-1)
