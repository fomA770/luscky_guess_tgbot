from copy import deepcopy
import random
from database.database import index

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove, InlineKeyboardMarkup
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON, LEXICON_COMMANDS, GIFS
from keyboards.play_finish import create_play_finish_keyboard
from keyboards.game_boards import *

user_router = Router()


@user_router.message(CommandStart())
async def process_start_command(message: Message, db: dict):
    db["users"][message.from_user.id] = deepcopy(db["user_status"])
    await message.answer(
        text=LEXICON_COMMANDS[message.text],
        reply_markup = create_play_finish_keyboard(finish = False)
    )


@user_router.message(Command(commands="help"))
async def process_help_command(message: Message, db):
    if db["users"][message.from_user.id]["in_game"]:
        await message.answer(
            text=LEXICON_COMMANDS[message.text],
            reply_markup=ReplyKeyboardRemove()
        )
    else:
        await message.answer(
            text=f'{LEXICON_COMMANDS[message.text]}\nСыграем?',
            reply_markup=create_play_finish_keyboard(finish = False)
        )


@user_router.message(Command(commands="rules"))
async def process_rules_command(message: Message, db):
    if db["users"][message.from_user.id]["in_game"]:
        await message.answer(
            text=LEXICON_COMMANDS[message.text],
            reply_markup=ReplyKeyboardRemove()
        )
    else:
        await message.answer(
            text=f'{LEXICON_COMMANDS[message.text]}\nСыграем?',
            reply_markup=create_play_finish_keyboard(finish = False)
        )

@user_router.message(Command(commands="balance"))
async def process_balance_command(message: Message, db: dict):
    if db["users"][message.from_user.id]["in_game"]:
        await message.answer(
            text = f'{LEXICON_COMMANDS['/balance']} {db['users'][message.from_user.id]['balance']}',
            reply_markup=ReplyKeyboardRemove()
        )
    else:
        await message.answer(
            text = f'{LEXICON_COMMANDS['/balance']} {db['users'][message.from_user.id]['balance']}, сыграем?',
            reply_markup=create_play_finish_keyboard(finish = False),
        )


@user_router.message(F.text == LEXICON['play'])
async def let_choose_side(message: Message, db: dict):
    if db["users"][message.from_user.id]["in_game"]:
        await message.answer(
        text=LEXICON['already_in_game'],
    )
    else:
        await message.answer(
            text=LEXICON['lets_play'],
            reply_markup=appoint_board_keyboard(),
        )

@user_router.message(F.text == LEXICON['finish'])
async def let_choose_side(message: Message, db: dict):
    db["users"][message.from_user.id]["in_game"] = False
    db["users"][message.from_user.id] = deepcopy(db["user_status"])
    await message.answer(
        text=LEXICON['stop_game'],
        reply_markup=ReplyKeyboardRemove(),
    )



@user_router.message(F.text.in_({"4", "5", "6"}))
async def process_board_appointment(message: Message, db: dict):
    db["users"][message.from_user.id]["in_game"] = True
    keyboard = create_game_board(int(message.text))
    db['users'][message.from_user.id]['game_board'] = keyboard
    db['users'][message.from_user.id]['balance'] -= index['cost']
    if db['users'][message.from_user.id]['balance'] < 0:
        db["users"][message.from_user.id]["in_game"] = False
        await message.answer(
        text="Упс! Кажется у тебя не хваатет денег.\nЧтобы начать игру снова нажми /start",
        reply_markup=ReplyKeyboardRemove()
    )
    else:
        await message.answer(
            text=f"Ты в игре. Баланс: {db['users'][message.from_user.id]['balance']}",
            reply_markup=InlineKeyboardMarkup(inline_keyboard = keyboard)
        )
        await message.answer(
            text = LEXICON['under_board_text'],
            reply_markup=ReplyKeyboardRemove()
        )
    #print(db)


@user_router.callback_query(F.data[:2] == "ok")
async def process_ok_click(callback: CallbackQuery, db: dict):

    #print(callback.from_user.id)
    multiply = db["users"][callback.from_user.id]["multiply"]
    amount = index[callback.data[-1]]["start"]
    db["users"][callback.from_user.id]["earned_in_game"] += amount + multiply
    db["users"][callback.from_user.id]["multiply"] += index[callback.data[-1]]["add"]

    #print(db["users"][callback.from_user.id]['earned_in_game'], db["users"][callback.from_user.id]["multiply"])

    i, j, side = map(int, callback.data.split('.')[1:])
    #print(db["users"][callback.from_user.id]['game_board'][i][j])
    db["users"][callback.from_user.id]['game_board'][i].pop(j)
    new_button = get_new_button(text = LEXICON['ok_button'])
    db["users"][callback.from_user.id]['game_board'][i].insert(j, new_button)
    #print(db["users"][callback.from_user.id]['game_board'][i][j])

    await callback.message.edit_text(
        text=(
            f'{random.choice(LEXICON["right_click"])}. ' 
            f'Заработано в игре: {db['users'][callback.from_user.id]['earned_in_game']}\n'
            f'В следующем подарке: {index[str(side)]['start'] + db['users'][callback.from_user.id]['multiply']}'
            ),
        reply_markup=InlineKeyboardMarkup(inline_keyboard = db["users"][callback.from_user.id]['game_board'])
    )

@user_router.callback_query(F.data[:4] == "bomb")
async def process_bomb_click(callback: CallbackQuery, db: dict, main_bot):

    db["users"][callback.from_user.id]["in_game"] = False

    i, j, side = map(int, callback.data.split('.')[1:])
    db["users"][callback.from_user.id]['game_board'][i].pop(j)
    new_button = get_new_button(text = LEXICON['bomb_button'])
    db["users"][callback.from_user.id]['game_board'][i].insert(j, new_button)

    print(db['users'][callback.from_user.id]['earned_in_game'])
    print(db['users'][callback.from_user.id]['multiply'])

    db['users'][callback.from_user.id]['earned_in_game'] = 0
    db['users'][callback.from_user.id]['multiply'] = 0

    change_to_nonactive_keyboard(db['users'][callback.from_user.id]['game_board'])

    await callback.message.edit_text(
        text=random.choice(LEXICON["wrong_click"]),
        reply_markup=InlineKeyboardMarkup(inline_keyboard = db['users'][callback.from_user.id]['game_board'])
    )

    await main_bot.send_sticker(
        chat_id = callback.from_user.id,
        sticker = random.choice(GIFS['bomb'])
    )

    await main_bot.send_message(
        chat_id = callback.from_user.id,
        text = f'Играем еще?\n\nТвой баланс составляет <b>{str(db['users'][callback.from_user.id]['balance'])}</b>',
        reply_markup = create_play_finish_keyboard()
    )

@user_router.callback_query(F.data == 'take_money')
async def process_balance_upgrade(callback: CallbackQuery, db: dict, main_bot):

    db["users"][callback.from_user.id]["in_game"] = False

    change_to_nonactive_keyboard(db['users'][callback.from_user.id]['game_board'])

    db['users'][callback.from_user.id]['balance'] += db['users'][callback.from_user.id]['earned_in_game']
    db['users'][callback.from_user.id]['earned_in_game'] = 0
    db['users'][callback.from_user.id]['multiply'] = 0

    await callback.message.edit_text(
        text=LEXICON["take_money_click"],
        reply_markup=InlineKeyboardMarkup(inline_keyboard = db['users'][callback.from_user.id]['game_board'])
    )

    if db['users'][callback.from_user.id]['balance'] >= 1500:
        await main_bot.send_sticker(
            chat_id = callback.from_user.id,
            sticker = random.choice(GIFS['ok'])
        )
        await main_bot.send_message(
            chat_id = callback.from_user.id,
            text = f'МОЛОДЦОМ! ТЫ ПОДНЯЛ БАБЛА\n\nЧтобы сыграть заново нажми /start или "Начать"',
            reply_markup = create_play_finish_keyboard(finish = False)
        )
        db["users"][callback.from_user.id] = deepcopy(db["user_status"])
    else:
        await main_bot.send_sticker(
            chat_id = callback.from_user.id,
            sticker = random.choice(GIFS['ok'])
        )
        await main_bot.send_message(
            chat_id = callback.from_user.id,
            text = f'Играем еще?\n\nТвой баланс составляет <b>{str(db['users'][callback.from_user.id]['balance'])}</b>',
            reply_markup = create_play_finish_keyboard()
        )


@user_router.callback_query(F.data == 'used')
async def process_used_button(callback: CallbackQuery):
    await callback.answer(text = 'Это поле больше неактивно...')