from random import choice

board_dict = {
    'a1': ' ',
    'a2': ' ',
    'a3': ' ',
    'b1': ' ',
    'b2': ' ',
    'b3': ' ',
    'c1': ' ',
    'c2': ' ',
    'c3': ' '
}

num_players = input('1 or 2 players? ')


def two_players():

    game_on = True
    turn = 0
    while game_on:
        if turn % 2 == 0:
            mark = 'X'
        else:
            mark = "O"
        board = f'\n  1   2   3\na {board_dict["a1"]} | {board_dict["a2"]} | {board_dict["a3"]} \n -----------\nb ' \
                f'{board_dict["b1"]} | {board_dict["b2"]} | {board_dict["b3"]} \n -----------\nc {board_dict["c1"]} ' \
                f'| {board_dict["c2"]} | {board_dict["c3"]} '
        print(board)
        place = input(f"\nPlayer {mark}, do you claim a spot or do you yield (letter then number)? ").lower()

        if place == 'I yield':
            if mark == 'X':
                mark = 'O'
            else:
                mark = 'X'
            print(f'\nCongratulations Player {mark}! Your opponent admits defeat and you have won!')
            game_on = False

        elif place in board_dict.keys():
            if board_dict[place] == ' ':
                turn += 1
                board_dict[place] = mark

                if board_dict['a1'] == board_dict['a2'] == board_dict['a3'] == mark \
                        or board_dict['b1'] == board_dict['b2'] == board_dict['b3'] == mark \
                        or board_dict['c1'] == board_dict['c2'] == board_dict['c3'] == mark \
                        or board_dict['a1'] == board_dict['b1'] == board_dict['c1'] == mark \
                        or board_dict['a2'] == board_dict['b2'] == board_dict['c2'] == mark \
                        or board_dict['a3'] == board_dict['b3'] == board_dict['c3'] == mark \
                        or board_dict['a1'] == board_dict['b2'] == board_dict['c3'] == mark \
                        or board_dict['a3'] == board_dict['b2'] == board_dict['c1'] == mark:
                    print(f'\n {board_dict["a1"]} | {board_dict["a2"]} | {board_dict["a3"]} \n-----------\n '
                          f'{board_dict["b1"]} | {board_dict["b2"]} | {board_dict["b3"]} \n-----------\n '
                          f'{board_dict["c1"]} | {board_dict["c2"]} | {board_dict["c3"]}\nCongratulations Player '
                          f'{mark}! You have won!')
                    game_on = False

                elif " " not in board_dict.values():
                    print(f'\n {board_dict["a1"]} | {board_dict["a2"]} | {board_dict["a3"]} \n-----------\n '
                          f'{board_dict["b1"]} | {board_dict["b2"]} | {board_dict["b3"]} \n-----------\n '
                          f'{board_dict["c1"]} | {board_dict["c2"]} | {board_dict["c3"]}\nIt is a draw!')
                    game_on = False

            else:
                print('\nThat spot is already taken. Please choose another.')

        else:
            print('\nThat is not a valid place')


def single_player():
    game_on = True
    turn = 0
    while game_on:
        if turn % 2 == 0:
            mark = 'X'
            board = f'\n  1   2   3\na {board_dict["a1"]} | {board_dict["a2"]} | {board_dict["a3"]} ' \
                    f'\n -----------\nb {board_dict["b1"]} | {board_dict["b2"]} | {board_dict["b3"]} ' \
                    f'\n -----------\nc {board_dict["c1"]} | {board_dict["c2"]} | {board_dict["c3"]} '
            print(board)
            place = input(f"\nPlayer {mark}, do you claim a spot or do you yield (letter then number)? ").lower()
            if place == 'I yield':
                if mark == 'X':
                    mark = 'O'
                else:
                    mark = 'X'
                print(f'\nCongratulations Player {mark}! Your opponent admits defeat and you have won!')
                game_on = False
            elif place in board_dict.keys():
                if board_dict[place] == ' ':
                    turn += 1
                    board_dict[place] = mark

                    if board_dict['a1'] == board_dict['a2'] == board_dict['a3'] == mark \
                            or board_dict['b1'] == board_dict['b2'] == board_dict['b3'] == mark \
                            or board_dict['c1'] == board_dict['c2'] == board_dict['c3'] == mark \
                            or board_dict['a1'] == board_dict['b1'] == board_dict['c1'] == mark \
                            or board_dict['a2'] == board_dict['b2'] == board_dict['c2'] == mark \
                            or board_dict['a3'] == board_dict['b3'] == board_dict['c3'] == mark \
                            or board_dict['a1'] == board_dict['b2'] == board_dict['c3'] == mark \
                            or board_dict['a3'] == board_dict['b2'] == board_dict['c1'] == mark:
                        print(
                            f'\n {board_dict["a1"]} | {board_dict["a2"]} | {board_dict["a3"]} '
                            f'\n-----------\n {board_dict["b1"]} | {board_dict["b2"]} | {board_dict["b3"]} '
                            f'\n-----------\n {board_dict["c1"]} | {board_dict["c2"]} | {board_dict["c3"]}\n'
                            f'Congratulations Player {mark}! You have won!')
                        game_on = False

                    elif " " not in board_dict.values():
                        print(
                            f'\n {board_dict["a1"]} | {board_dict["a2"]} | {board_dict["a3"]} '
                            f'\n-----------\n {board_dict["b1"]} | {board_dict["b2"]} | {board_dict["b3"]} '
                            f'\n-----------\n {board_dict["c1"]} | {board_dict["c2"]} | {board_dict["c3"]}\n'
                            f'It is a draw!')
                        game_on = False

                else:
                    print('\nThat spot is already taken. Please choose another.')

            else:
                print('\nThat is not a valid place')

        else:
            place = None
            open_spot = False
            mark = "O"
            while not open_spot:
                place = choice(list(board_dict.keys()))
                if board_dict[place] != ' ':
                    open_spot = False
                else:
                    open_spot = True
            board_dict[place] = mark
            turn += 1
            if board_dict['a1'] == board_dict['a2'] == board_dict['a3'] == mark or board_dict['b1'] == board_dict[
                'b2'] == board_dict['b3'] == mark or board_dict['c1'] == board_dict['c2'] == board_dict[
                'c3'] == mark or board_dict['a1'] == board_dict['b1'] == board_dict['c1'] == mark or board_dict[
                'a2'] == board_dict['b2'] == board_dict['c2'] == mark or board_dict['a3'] == board_dict['b3'] == \
                    board_dict['c3'] == mark or board_dict['a1'] == board_dict['b2'] == board_dict['c3'] == mark or \
                    board_dict['a3'] == board_dict['b2'] == board_dict['c1'] == mark:
                print(
                    f'\n {board_dict["a1"]} | {board_dict["a2"]} | {board_dict["a3"]} '
                    f'\n-----------\n {board_dict["b1"]} | {board_dict["b2"]} | {board_dict["b3"]} '
                    f'\n-----------\n {board_dict["c1"]} | {board_dict["c2"]} | {board_dict["c3"]}\n'
                    f'Congratulations Player {mark}! You have won!')
                game_on = False

            elif " " not in board_dict.values():
                print(
                    f'\n {board_dict["a1"]} | {board_dict["a2"]} | {board_dict["a3"]} '
                    f'\n-----------\n {board_dict["b1"]} | {board_dict["b2"]} | {board_dict["b3"]} '
                    f'\n-----------\n {board_dict["c1"]} | {board_dict["c2"]} | {board_dict["c3"]}\n'
                    f'It is a draw!')
                game_on = False


valid_num = False
while not valid_num:
    if num_players == '2':
        valid_num = True
        two_players()

    elif num_players == '1':
        valid_num = True
        single_player()

    else:
        print('Please enter "1" or "2"')
        num_players = input('1 or 2 players? ')
