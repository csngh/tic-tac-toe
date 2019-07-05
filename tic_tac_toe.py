'''
Coding Practice
Tic Tac Toe
12.01.2018
'''

index_values_dictionary = {1: [0, 0], 2: [0, 1], 3: [0, 2],
                           4: [1, 0], 5: [1, 1], 6: [1, 2],
                           7: [2, 0], 8: [2, 1], 9: [2, 2]
                           }

board_status_list = [[' ', ' ', ' '],
                     [' ', ' ', ' '],
                     [' ', ' ', ' ']
                     ]

winning_pattern = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]


def display_board():
    print('\n' * 50)
    print('\n\n')
    print('     |     |     ')
    print('  {x}  |  {y}  |  {z}  '.format(x=board_status_list[0][0], y=board_status_list[0][1],
                                           z=board_status_list[0][2]))
    print('_____|_____|_____')
    print('     |     |     ')
    print('  {x}  |  {y}  |  {z}  '.format(x=board_status_list[1][0], y=board_status_list[1][1],
                                           z=board_status_list[1][2]))
    print('_____|_____|_____')
    print('     |     |     ')
    print('  {x}  |  {y}  |  {z}  '.format(x=board_status_list[2][0], y=board_status_list[2][1],
                                           z=board_status_list[2][2]))
    print('     |     |     ')
    print('\n')


def calculate_win(lab):
    pattern_list = []

    for index_of_board in range(1, 10):
        index_calculated = index_values_dictionary[index_of_board]
        if board_status_list[index_calculated[0]][index_calculated[1]] == lab:
            pattern_list.append(index_of_board)
        else:
            continue

    final_set = set(pattern_list)

    for i in winning_pattern:
        lst = list(final_set & set(i))
        lst.sort()
        if lst == i:
            return True
        else:
            continue
    else:
        return False


def play_game():
    player_x = input("\nEnter player X's name: ")
    player_o = input("\nEnter player O's name: ")

    taken_index = []

    display_board()

    vals = {True: 'X', False: 'O'}
    bl = True
    param = vals[bl]

    jump_out = False
    while not jump_out:
        print("\n\nPlayer: ", player_x if bl else player_o, "'s turn")
        choice = input('\nPlaces (1 - 9)'
                       '\n(q to quit):  ')

        if choice == 'q':
            jump_out = True
        elif choice != 'q':
            index = int(choice)
            if 0 < index < 10:

                if len(taken_index) == 0:
                    taken_index.append(index)
                    index_list_user = index_values_dictionary[index]
                    board_status_list[index_list_user[0]][index_list_user[1]] = param
                    display_board()
                    win_x = calculate_win('X')
                    win_o = calculate_win('O')

                    if win_x:
                        jump_out = True
                        print(player_x, ' won !!')
                        print(player_o, ' better luck next time.')
                        break
                    elif win_o:
                        jump_out = True
                        print(player_o, ' won !!')
                        print(player_x, ' better luck next time.')
                        break

                    bl = not bl
                    param = vals[bl]

                else:
                    for i in taken_index:
                        if i == index:
                            display_board()
                            print('Place already taken, try another one')
                            break
                        else:
                            continue
                    else:
                        taken_index.append(index)
                        index_list_user = index_values_dictionary[index]
                        board_status_list[index_list_user[0]][index_list_user[1]] = param
                        display_board()
                        win_x = calculate_win('X')
                        win_o = calculate_win('O')

                        if len(taken_index) == 9:
                            if not win_x and not win_o:
                                print("It's a tie, try again folks")
                                jump_out = True
                                break

                        if win_x:
                            jump_out = True
                            print(player_x, ' won !!')
                            print(player_o, ' better luck next time.')
                            break
                        elif win_o:
                            jump_out = True
                            print(player_o, ' won !!')
                            print(player_x, ' better luck next time.')
                            break
                        bl = not bl
                        param = vals[bl]


            else:
                print('Wrong index number try again.....\n\n\n')
        else:
            print('Invalid Choice')


play_game()
