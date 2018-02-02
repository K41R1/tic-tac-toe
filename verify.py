# -*- coding: utf-8 -*-
import board
import sys


def verify_line(player, l):
    i = 0
    for v in board.board[l]:
        if v == player:
            i += 1
    if i == 3:
        print("player " + player + " win")
        sys.exit(0)


def verify_column(player, l):
    i = 0
    while i < 3 and board.board[i][l] == player:
        i += 1
    if i == 3:
        print("player " + player + " win")
        sys.exit(0)


def verify_first_diag(player):
    i = 0
    while i < 3 and board.board[i][i] == player:
        i += 1
    if i == 3:
        print("player " + player + " win")
        sys.exit(0)


def verify_second_diag(player):
    i = 0
    while i < 3 and board.board[i][2 - i] == player:
        i += 1
    if i == 3:
        print("player " + player + " win")
        sys.exit(0)
