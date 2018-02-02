#!/usr/bin/env python3

import sys
import board
import verify

player = 0
players = {
    'player1': '\033[31;01mX\033[0m',
    'player2': '\033[32;01mO\033[0m'
}
current_player = {
    'player1': False,
    'player2': False
}


def switchPlayers():
    global current_player
    current_player['player1'] = not current_player['player1']
    current_player['player2'] = not current_player['player2']


def play():
    print("choose position ..")
    ln = int(input("line == "))
    col = int(input("column == "))
    board.put(current_player, ln, col)
    board.printBoard()
    switchPlayers()
    test('\033[31;01mX\033[0m')
    test('\033[32;01mO\033[0m')


def test(player):
    verify.verify_line(player, 0)
    verify.verify_line(player, 1)
    verify.verify_line(player, 2)
    verify.verify_column(player, 0)
    verify.verify_column(player, 1)
    verify.verify_column(player, 2)
    verify.verify_first_diag(player)
    verify.verify_second_diag(player)


def main():
    board.initBoard()
    try:
        global player
        player = int(input("choose the first player [1/2]"))
    except:
        sys.exit("\033[31;01mMUST\033[00m be INT")
    current_player['player' + str(player)] = True
    while True:
        play()

# just run if execute from the interpreter


if __name__ == '__main__':
    main()
