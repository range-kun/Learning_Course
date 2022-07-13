from itertools import cycle, chain
import copy


def x_o():
    n = 1
    while True:
        field = [3 * [' '] for _ in range(3)]
        players = {'x': 'Игрок 1', 'o': 'Игрок 2'}
        sign = cycle(players)
        print(f'\n === Игра №{n} === \n')
        print(show_field(field))
        play_the_game(sign, players, field)
        x = input('Нажмите Y/y для повторной игры: ')
        if x not in ['Y', 'y']:
            print('Спасибо за игру!')
            break
        n += 1


def show_field(field):
    board = copy.deepcopy(field)
    line = '\n'+8*'-'+'\n'
    for i in range(3):
        board[i].insert(0, str(i))
    board.insert(0, [' ', '0', '1', '2'])
    return line.join(['|'.join(i)+'|' for i in board])+line


def play_the_game(sign, players, field):
    while True:
        turn = next(sign)
        coord = input(f'Ходит {players[turn]}. Введите номер ряда и строки через пробел: ').split()
        coord = list(map(int, coord))
        if len(coord) != 2 or coord[0] > 2 or coord[1] > 2:
            print('Пожалуйста введите правильное значение!')
            turn = next(sign)
            continue
        if field[coord[0]][coord[1]] != ' ':
            print('Ячейка уже занята, выберите пустую!')
            turn = next(sign)
            continue
        field[coord[0]][coord[1]] = turn
        print(show_field(field))
        result = check_win_condition(field)
        if result == 'Victory':
            print(f'{players[turn]} победил')
            break
        elif result == 'Tie':
            print('Боевая ничья')
            break


def check_win_condition(field):
    field = list(chain(*field))
    for a, b, c in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                    (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
        if field[a] == field[b] == field[c] != ' ':
            return 'Victory'
    if all(i != ' ' for i in field):
        return 'Tie'
    else:
        return


if __name__ == '__main__':
    x_o()
