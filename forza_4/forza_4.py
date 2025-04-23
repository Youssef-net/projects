def board_printer(board):
    """
    Stampa il tabellone di gioco in modo allineato e ben formattato,
    tenendo conto delle emoji che occupano più spazio.
    """
    for row in board:
        print(" | ".join(f"{cell}" if cell != " " else "⬜" for cell in row))  # Usa "⬜" per celle vuote
        print("-" * 29)  # Linea divisoria ben proporzionata
    print("  1   2   3   4   5   6   7")  # Numerazione delle colonne

# funzione che chiede al giocatore 1 il proprio nome e scelta colore
def player_1()->str:
    name = ""
    color = ""
    while len(name) < 3: 
        name = input("Gioacatore 1, inserisci un nome di almeno 3 caratteri: ")
    while color != "rosso" and color != "blu":
        color = input("Scegli colore, blu o rosso: ")
        
    return name, color 

""" Funzione che chiede al giocatore numero 2 di inserire il proprio nome e prende in input il colore del giocatore 1 
    E restituisce il nome del giocatore 2. E il colore della sua pallina, in base alla scelta del primo giocatore"""

def player_2(player1_color)->str:
    name = ""
    while len(name) < 3: 
        name = input("Gioacatore 2, inserisci un nome di almeno 3 caratteri: ")
    if player1_color == "blu":
        color = "rosso"

    else:
        color = "blu"
    return name, color

def circle_color(color_choice):
    if color_choice == "rosso":
        retvalue = "🔴"
    else:
        retvalue = "🔵"

    return retvalue

def game_move(board):

    column = 0
    while column < 1 or column > len(board)+1 or board [0][column-1]!= " ":
        board_printer(board)
        try:
            column = int(input("Inserisci colonna: "))
            if column < 1 or column > len(board)+1 or board [0][column-1]!= " ":
                print("Posizione occupata") 
        except:
            print("Inserisci numero intero")
    
    
    row = len(board) -1 # supongo che la riga libera sia l'ultima
    if board[row] != " ":   # se l'ultima riga è occupata
        for i in range(len(board)-1): # cerco la riga libera
            if board[i][column-1] == " " and board[i+1][column -1] != " ": # se la riga i è libera e la riga sotto(i+1) è occupata
                row = i # allora la riga da occupare è la i
                break

    return row, column - 1 # restituisco la riga e la colonna, sottraggo 1 aòòa colonna perchè l'utente inserisce da 1 a 7 e non da 0 a 6

def winner_evaluation(board, row, column):
    counter_row = 0    
    counter_column = 0
    counter_main_diag = 0
    counter_second_diag = 0

    main_diag_column = 0
    second_diag_column = 0


    for i in range(len(board)):
        if board[i][column] == board[row][column]:
                counter_column += 1
                if counter_column == 4:
                    break
        else:
            counter_column = 0   
        
        main_diag_column = (column - row) + i
        second_diag_column = (column + row) - i
        
        if main_diag_column >= 0 and main_diag_column < len(board[i]) and board[i][main_diag_column] == board[row][column]:
            counter_main_diag += 1
            if counter_main_diag == 4:
                break  
        else:
            counter_main_diag = 0

        if second_diag_column >= 0 and second_diag_column < len(board[i]) and board[i][second_diag_column] == board[row][column]:
            counter_second_diag += 1
            if counter_second_diag == 4:
                break
        else:
            counter_second_diag = 0                          
        
    for j in range(len(board[i])):

        if board[row][j] == board[row][column]:
            counter_row +=1
            if counter_row == 4:
                break

        else:
            counter_row = 0    

        if counter_column == 4:
            break                           
         
    if counter_row == 4 or counter_column == 4 or counter_main_diag == 4 or counter_second_diag == 4: 
        return board[row][column]
    
    return None

def winner_printer(winner, color_1, color_2, player_1, player_2):
    if winner == color_1:
        print(f"{player_1} Wins")
    elif winner == color_2:
        print(f"{player_2} Wins")
    elif winner == "draw":
        print("Draw!")         
    else:
        None

def engine(board, color_1, color_2, player_1, player_2):
    turn = 1
    winner = None
    while winner == None:
        if turn == 43:
            print("draw")
            break
        if turn % 2 == 0:
            print(f"{player_2} Toocca a te")
            row, column = game_move(board)
            board[row][column] = color_2
            winner = winner_evaluation(board, row, column)
        else:
            print(f"{player_1} Toocca a te")
            row,column = game_move(board)
            board[row][column] = color_1
            winner = winner_evaluation(board, row, column)
            #winner_printer winner, color_1, color_2, player_1, player_2)
         
        turn += 1 

    board_printer(board)
    winner_printer (winner, color_1, color_2, player_1, player_2)

def main():
    player_1_name , player_1_color = player_1()
    player_2_name, player_2_color = player_2(player_1_color)
    color_1 = circle_color(player_1_color)
    color_2 = circle_color(player_2_color)
    board = [[" "for i in range(7)] for j in range(6)]
    engine(board, color_1, color_2, player_1_name, player_2_name)
    
if __name__== "__main__":
    main()


#print(len(matrix), matrix)

