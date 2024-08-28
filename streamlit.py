import streamlit as st
def printboard(xstate, zstate):
    zero = 'x' if xstate[0] else ('0' if zstate[0] else 0)
    one = 'x' if xstate[1] else ('0' if zstate[1] else 1)
    two = 'x' if xstate[2] else ('0' if zstate[2] else 2)
    three = 'x' if xstate[3] else ('0' if zstate[3] else 3)
    four = 'x' if xstate[4] else ('0' if zstate[4] else 4)
    five = 'x' if xstate[5] else ('0' if zstate[5] else 5)
    six = 'x' if xstate[6] else ('0' if zstate[6] else 6)
    seven = 'x' if xstate[7] else ('0' if zstate[7] else 7)
    eight = 'x' if xstate[8] else ('0' if zstate[8] else 8)
    print(f"{zero} | {one} | {two}")
    print(f"{three} | {four} | {five}")
    print(f"{six} | {seven} | {eight}")

def checkwin(xstate, zstate):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    
    for win in wins:
        if (xstate[win[0]] + xstate[win[1]] + xstate[win[2]]) == 3:
            print("X's won the match")
            return 1
        if (zstate[win[0]] + zstate[win[1]] + zstate[win[2]]) == 3:
            print("O's won the match")
            return 0
    
    return -1

if __name__ == "__main__":
    xstate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zstate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1
    print("Welcome to Tic Tac Toe")
    
    while True:
        printboard(xstate, zstate)
        
        if turn == 1:
            print("X's chance")
            value = int(input("Please enter a value (0-8): "))
            xstate[value] = 1
        else:
            print("O's chance")
            value = int(input("Please enter a value (0-8): "))
            zstate[value] = 1
        
        cwin = checkwin(xstate, zstate)
        if cwin != -1:
            print("Match over")
            break
        
        turn = 1 - turn
