# Langkah 1 : Bina board menggunakan dictionary "theBoard"

theBoard = {'1':' ','2':' ','3':' ',
            '4':' ','5':' ','6':' ',
            '7':' ','8':' ','9':' '}

# Langkah 2 : Cipta Function "printBoard()" untuk print keadaan semasa untuk setiap pusingan

def printBoard(board):
  print(board["1"]+'|'+board["2"]+'|'+board["3"])
  print("-+-+-")
  print(board["4"]+'|'+board["5"]+'|'+board["6"])
  print("-+-+-")
  print(board["7"]+'|'+board["8"]+'|'+board["9"])

# Langkah 3 : Cipta Function "game()" untuk Game TicTacToe

def game():

  # Langkah 4 : Cipta variable "Turn" (Giliran X atau O) dan variable "count" untuk kiraan pusingan
  turn = 'X'
  count = 0

  # Langkah 5 : Cipta while loop supaya game berjalan sampai ada pemenang atau pusingan 9

  while True:
    printBoard(theBoard)
    print("Giliran "+ turn + ", pilih petak kosong")

    # Langkah 6 : Cipta varibale "move" dimana user akan masukkan nombor petak yang diingini

    move = input()

    # Langkah 7 : Semak sama ada petak telah dipenuhi atau tidak menggunakan if else condition.

    if theBoard[move] == " ":
      theBoard[move] = turn
      count = count + 1
    else:
      print("Petak telah dipilih! Sila pilih petak lain")
      continue
    
    # Langkah 8 : Semak sama ada sudah ada pemenang selepas 5 pusingan. terdapat 8 cara untuk menang. print board terakhir

    if count >= 5:
      #horizontal
      if theBoard["1"] == theBoard["2"] == theBoard["3"] != " ":
        printBoard(theBoard)
        print("Game over. Player "+ turn + " win!!!")
        break
      elif theBoard["4"] == theBoard["5"] == theBoard["6"] != " ":
        printBoard(theBoard)
        print("Game over. Player "+ turn + " win!!!")
        break
      elif theBoard["7"] == theBoard["8"] == theBoard["9"] != " ":
        printBoard(theBoard)
        print("Game over. Player "+ turn + " win!!!")
        break
      #vertical
      elif theBoard["1"] == theBoard["4"] == theBoard["7"] != " ":
        printBoard(theBoard)
        print("Game over. Player "+ turn + " win!!!")
        break
      elif theBoard["2"] == theBoard["5"] == theBoard["8"] != " ":
        printBoard(theBoard)
        print("Game over. Player "+ turn + " win!!!")
        break
      elif theBoard["3"] == theBoard["6"] == theBoard["9"] != " ":
        printBoard(theBoard)
        print("Game over. Player "+ turn + " win!!!")
        break
      #diagonal
      elif theBoard["1"] == theBoard["5"] == theBoard["9"] != " ":
        printBoard(theBoard)
        print("Game over. Player "+ turn + " win!!!")
        break
      elif theBoard["3"] == theBoard["5"] == theBoard["7"] != " ":
        printBoard(theBoard)
        print("Game over. Player "+ turn + " win!!!")
        break

    
    # Langkah 9 : Seri jika tiada pemenang selepas 9 pusingan. print board terakhir
    if count == 9:
      printBoard(theBoard)
      print("Seri. Tiada pemenang")
      break
    
    # Langkah 10 : Tukar giliran
    if turn == "X":
      turn = "O"
    else:
      turn = "X"

if __name__ == "__main__":
  game()



















