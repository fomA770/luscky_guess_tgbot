LEXICON_COMS_DESC = {
    '/start': 'Начать (перезапустить) игру',

    '/help': "Информация о боте",

    '/rules':"Правила игры",

    '/balance': "Узнать баланс"
}

LEXICON_COMMANDS = {
    '/start': "<b>Сыграем в минное поле?</b>\n\n"
              "Чтобы узнать правила игры, отправь /help",

    '/help':"Информация по игре <b>'минное поле'</b>:\n\n"
            "Доступные команды:\n"
            "/rules - узнать правила игры\n"
            "/balance - узнать текущий баланс",

    '/rules':"На поле заданных вами размеров лежат подарки🎁.\n<b>Открывайте их!</b>\n"
             "Достали деньги - заработали,\nДостали бомбу - потеряли всё\n"
             "Не уверены в своей удаче - забирайте выигрыш\n\n"
             "Чем больше поле, тем больше денег в подарках\n"
             "Тем больше шанс проиграть\n\n"
             "Ваша начальная сумма = <b>1250.</b>\n"
             "Стоимость одной игры - <b>250 руб.</b>\n" 
             "Для победы вам потребуется поднять бабла и заработать <b>3000</b>",

    '/balance': "Ваш текущий баланс составляет: "
}

LEXICON = {
    'cant_handle_update': 'Я реагирую только на текст и нажатия на кнопки',
    'play': 'Играем',
    'finish': 'Закончить (обнулить баланс)',
    'standard_button': '🎁',
    'nonactive_buttons': ['💣', '💣', '💣', '💥', '💥', '🧨'], 
    'bomb_button': '💣',
    'ok_button': '💰',
    'right_click': ['Yessir! Guess another one', 'В яблочко', 'Фух, пронесло..'],
    'wrong_click': ['💣Bomb💣, you lost money!!!', '💣Бомба💣, ты потерял деньги', '💣! Be more lucky next time...💣'],
    'take_money_click': 'Выигрыш получен!🎁',
    'under_board_text': '💥Не трогай бомбы!💥',
    'lets_play': "Выбери размер поля для игры.\nСтоимость игры: 250",
    'stop_game': 'Твой баланс обнулен.\nЕсли захочешь сыграть снова, отправь /start',
    'already_in_game': 'Вы уже выбрали поле'

}

GIFS = {
    'unknown': [
        "CAACAgIAAxkBAAMuaYJP3By5F8WIX0ZApvt8cKkmEN0AArOAAALw9yFJrRpkfKozW8Q4BA",

    ],
    'bomb': [
        "CAACAgIAAxkBAAMwaYJQDz7hFFPkJEl_WwlAaaQ9TYAAAtFmAAK6Q6lJ7tDwnqT6gyE4BA",
        "CAACAgIAAxkBAAMxaYJQypDaoXcu-S_FQnkDi1bW39oAAi4dAAIqeOFKB_r-u6AhyiA4BA",
        "CAACAgIAAxkBAAMyaYJQ1OcRkf28s_4yrykoLh5GaNIAAscqAAIohdhIWDDmAzIZgNs4BA",
        "CAACAgIAAxkBAAMzaYJQ1qgAAUAtkh6XQIwDibqOFK7CAAJTKAACd0q5SWKj64fQzglVOAQ",
        "CAACAgIAAxkBAAM0aYJRCT3kojJ9uNZsjjneAl84zxQAAtcPAAKSO_lI2GLgvE_ZV7Q4BA"
    ],
    'ok': [
        "CAACAgIAAxkBAAM5aYJTtIAJYt9_W08cxCM5hJdO5ecAAuEXAAJCrEBJwIoQcyQwCsM4BA",
        "CAACAgIAAxkBAAM4aYJTqWhKAYc9whSNkZ3TrEcngTQAAvkYAAKSvfhIcDmIMr41R0Y4BA",
        "CAACAgIAAxkBAAM1aYJTWmR1UlQ3uw2hfiGHxMpqvaQAAgwYAAJB_oFJsxnc0yZF09I4BA",
        "CAACAgIAAxkBAAM7aYJUm2LSZhpNKMkdKITAp2NPnrYAAv4ZAAJNqgFIEXFO1SWWME44BA",
        "CAACAgIAAxkBAAM6aYJUEfJxs7mQss40fc-Q66NM1hkAArohAAIW-LFK-ckxDl_vNyQ4BA"
    ],
    'win': "CgACAgIAAxkBAAIBvmmCX3LQrkvleizoLtdomXoFdlD3AAJ0RwACDb04S-Ksu9xm4Sh7OAQ",
}

#print(len(LEXICON_COMMANDS['/rules']))