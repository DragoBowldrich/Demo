field_content = ' ' * 9
cells_list = [x for x in field_content]
play_grid = [cells_list[0:3], cells_list[3:6], cells_list[6:10]]

# Print empty grid


def empty_grid():
    print('---------')
    print('|', play_grid[0][0], play_grid[0][1], play_grid[0][2], '|')
    print('|', play_grid[1][0], play_grid[1][1], play_grid[1][2], '|')
    print('|', play_grid[2][0], play_grid[2][1], play_grid[2][2], '|')
    print('---------')


empty_grid()


def check_horizontals_1():
    global play_grid
    if play_grid[0][0] == play_grid[0][1] and play_grid[0][0] == play_grid[0][2] and ' ' not in play_grid[0]:
        print(play_grid[0][0], 'wins')
        return True


def check_horizontals_2():
    global play_grid
    if play_grid[1][0] == play_grid[1][1] and play_grid[1][0] == play_grid[1][2] and ' ' not in play_grid[1]:
        print(play_grid[1][0], 'wins')
        return True


def check_horizontals_3():
    global play_grid
    if play_grid[2][0] == play_grid[2][1] and play_grid[2][0] == play_grid[2][2] and ' ' not in play_grid[2]:
        print(play_grid[2][0], 'wins')
        return True


def check_verticals_1():
    global play_grid
    if play_grid[0][0] == play_grid[1][0] and play_grid[0][0] == play_grid[2][0] and ' ' not in play_grid[0][0]:
        print(play_grid[0][0], 'wins')
        return True


def check_verticals_2():
    global play_grid
    if play_grid[0][1] == play_grid[1][1] and play_grid[0][1] == play_grid[2][1] and ' ' not in play_grid[0][1]:
        print(play_grid[0][1], 'wins')
        return True


def check_verticals_3():
    global play_grid
    if play_grid[0][2] == play_grid[1][2] and play_grid[0][2] == play_grid[2][2] and ' ' not in play_grid[0][2]:
        print(play_grid[0][2], 'wins')
        return True


def check_diagonals_1():
    global play_grid
    if play_grid[0][0] == play_grid[1][1] and play_grid[0][0] == play_grid[2][2] and ' ' not in play_grid[0][0]:
        print(play_grid[0][0], 'wins')
        return True


def check_diagonals_2():
    global play_grid
    if play_grid[0][2] == play_grid[1][1] and play_grid[0][2] == play_grid[2][0] and ' ' not in play_grid[0][2]:
        print(play_grid[0][2], 'wins')
        return True


def check_draw():
    global play_grid
    if ' ' not in play_grid[0] and ' ' not in play_grid[1] and ' ' not in play_grid[2]:
        print('Draw')
        return True


def input_validation_x():
    global play_grid
    while True:
        play_grid_input = input('Enter the coordinates:').split()
        if len(play_grid_input) != 2:
            print('You should enter numbers!')
        elif not play_grid_input[0].isnumeric() and not play_grid_input[1].isnumeric():
            print('You should enter numbers!')
        elif int(play_grid_input[0]) not in [1, 2, 3] or int(play_grid_input[1]) not in [1, 2, 3]:
            print('Coordinates should be from 1 to 3!')
        elif play_grid[int(play_grid_input[0]) - 1][int(play_grid_input[1]) - 1] != ' ':
            print('This cell if occupied ! Choose another one!')
        else:
            move_x = [int(x) for x in play_grid_input]
            play_grid[move_x[0] - 1][move_x[1] - 1] = 'X'
            break


def input_validation_o():
    global play_grid
    while True:
        play_grid_input = input('Enter the coordinates:').split()
        if len(play_grid_input) != 2:
            print('You should enter numbers!')
        elif not play_grid_input[0].isnumeric() and not play_grid_input[1].isnumeric():
            print('You should enter numbers!')
        elif int(play_grid_input[0]) not in [1, 2, 3] or int(play_grid_input[1]) not in [1, 2, 3]:
            print('Coordinates should be from 1 to 3!')
        elif play_grid[int(play_grid_input[0]) - 1][int(play_grid_input[1]) - 1] != ' ':
            print('This cell if occupied ! Choose another one!')
        else:
            move_x = [int(x) for x in play_grid_input]
            play_grid[move_x[0] - 1][move_x[1] - 1] = 'O'
            break


while check_horizontals_1() or check_horizontals_2() or check_horizontals_3() or \
        check_verticals_1() or check_verticals_2() or check_verticals_3() or check_diagonals_1() or check_diagonals_2() is not True:

    input_validation_x()


    def active_grid():
        print('---------')
        print('|', play_grid[0][0], play_grid[0][1], play_grid[0][2], '|')
        print('|', play_grid[1][0], play_grid[1][1], play_grid[1][2], '|')
        print('|', play_grid[2][0], play_grid[2][1], play_grid[2][2], '|')
        print('---------')

    active_grid()

    if check_horizontals_1() or check_horizontals_2() or check_horizontals_3() or check_verticals_1() or check_verticals_2() or check_verticals_3() or check_diagonals_1() or check_diagonals_2():
        break

    elif check_draw():
        break

    input_validation_o()

    def active_grid():
        print('---------')
        print('|', play_grid[0][0], play_grid[0][1], play_grid[0][2], '|')
        print('|', play_grid[1][0], play_grid[1][1], play_grid[1][2], '|')
        print('|', play_grid[2][0], play_grid[2][1], play_grid[2][2], '|')
        print('---------')


    active_grid()
