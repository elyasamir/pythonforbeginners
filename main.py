#Two Player Tic-Tac-Toe game in Python.

# Langkah 1 : Bina board menggunakan dictionary "theBoard"

''' Bina board
                    1|2|3 
                    -+-+-
                    4|5|6 
                    -+-+-
                    7|8|9            '''

theBoard = {'1': ' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }

# Langkah 2 : Cipta Function "printBoard()" untuk print keadaan semasa untuk setiap pusingan

def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

# Langkah 3 : Cipta Function "game()" untuk Game TicTacToe

def game():

    # Langkah 4 : Cipta variable "Turn" (Giliran X atau O) dan variable "count" untuk kiraan pusingan
    turn = 'X'
    count = 0

    # Langkah 5 : Cipta for loop untuk 10 pusingan. Print keadaan semasa board
    for i in range(10):
        printBoard(theBoard)
        print("It's your turn," + turn + ".Move to which place?")

        # Langkah 6 : Cipta varibale "move" dimana user akan masukkan nombor petak yang diingini
        move = input()        

        # Langkah 7 : Semak sama ada petak telah dipenuhi atau tidak menggunakan if else condition. 
        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        # Langkah 8 : Semak sama ada sudah ada pemenang selepas 5 pusingan. terdapat 8 cara untuk menang.
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")                
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 

        # Langkah 9 : Seri jika tiada pemenang selepas 9 pusingan.
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")

        # Langkah 10 : Tukar giliran
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    

if __name__ == "__main__":
    game()