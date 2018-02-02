# -*- coding: utf-8 -*-
import sys

board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]


def initBoard():
    global board
    for line in board:
        for case in line:
            print('|' + case + '|', end='')
        print()
        for bar in range(0, 5):
            print('__', end='')
        print('\n')


def put(players, line, column):
    global board
    if players['player1'] is True:
        board[line][column] = "\033[31;01mX\033[0m"
    else:
        board[line][column] = "\033[32;01mO\033[0m"


def printBoard():
    sys.stdout.flush()
    global board
    for line in board:
        for case in line:
            print('|' + case + '|', end='')
        print()
        for bar in range(0, 5):
            print('__', end='')
        print('\n')
