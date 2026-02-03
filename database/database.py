def init_db():
    return {
        'users': {},
        'user_status': {
            'in_game': False,
            'balance': 1250,
            'earned_in_game': 0,
            'multiply': 0,
            'game_board': [],
        }
    }

index = {
            '4': {'start': 190, 'add': 60},
            '5': {'start': 175, 'add': 75},
            '6': {'start': 160, 'add': 90},
            'cost': 250
        }


'''
'users'= {

    '2312343151': 
    {
        'in_game': False, 'balance': 1200
    },

    '231234Ry3uh': 
    {
        'in_game': False, 'balance': 1200
    }
}

'''