"""Il giovo tris, si vince il primo che riesce a fare una linea orizzontale, verticale o diagonale di tre palline dello stesso colore
ogni giocatore inserisce il suo nome, e poi il primo giocatore sceglie il colore della sua pallina, il secondo giocatore avrà il colore opposto"""

# Stampa il tabellone di gioco con separatori

def board_printer(board):
    for row in board:
        for i in range(len(row)):
            if i < 2:
                print(row[i], end=" |")
            else:
                print(row[i], end="")
        print("\n--------")

# Funzione che chiede al giocatore 1 il proprio nome e la scelta del colore

def player_1()->str:
    name = ""
    color = ""
    while len(name) < 3: 
        name = input("Giocatore 1, inserisci un nome di almeno 3 caratteri: ")
    while color != "rosso" and color != "blu":
        color = input("Scegli colore, blu o rosso: ")
        
    return name, color 

# Funzione che chiede al giocatore 2 il proprio nome e assegna automaticamente un colore(in base alla scelta del primo giocatore)

def player_2(player1_color)->str:
    name = ""
    while len(name) < 3: 
        name = input("Giocatore 2, inserisci un nome di almeno 3 caratteri: ")
    
    # Assegna il colore opposto a quello scelto dal giocatore 1
    if player1_color == "blu":
        color = "rosso"
    else:
        color = "blu"
    return name, color

# Funzione che converte il colore testuale in un'emoji corrispondente

def circle_color(color_choice):
    if color_choice == "rosso":
        retvalue = "🔴"
    else:
        retvalue = "🔵"
    return retvalue

# Funzione per gestire l'inserimento della mossa di un giocatore

def game_move(board):
    row = 0
    column = 0
    while row < 1 or row > len(board) or column < 1 or column > len(board[row-1]) or board[row-1][column-1] != " ":
        board_printer(board)
        try:
            row = int(input(f"Inserisci riga: "))
            column = int(input("Inserisci colonna: "))
            if row < 1 or row > 3 or column < 1 or column > 3 or board[row-1][column-1] != " ":
                print("Posizione occupata") 
        except:
            print("Inserisci numero intero")

    return row - 1, column - 1

# Funzione per valutare se un giocatore ha vinto

def winner_evaluation(board, row, column):
    counter_row = 0    
    counter_column = 0
    counter_main_diag = 0
    counter_second_diag = 0
    
    for i in range(len(board)):
        if board[i][column] == board[row][column]:
            counter_column += 1
        if column == row and board[i][i] == board[row][column]:
            counter_main_diag += 1 
        if (column + row) == (len(board) - 1) and board[i][(len(board)-1) - i] == board[row][column]:
            counter_second_diag += 1
    
    for j_col in range(len(board)):
        if board[row][j_col] == board[row][column]:
            counter_row += 1
                 
    if counter_row == 3 or counter_column == 3 or counter_main_diag == 3 or counter_second_diag == 3: 
        return board[row][column]
    
    return None

# Funzione per stampare il vincitore

def winner_printer(winner, color_1, color_2, player_1, player_2):
    if winner == color_1:
        print(f"{player_1} Wins")
    elif winner == color_2:
        print(f"{player_2} Wins")
    elif winner == "draw":
        print("Draw!")         
    else:
        None

# Funzione che gestisce il flusso di gioco

def engine(board, color_1, color_2, player_1, player_2):
    turn = 1
    winner = None
    while winner is None:
        if turn == 10:
            print("Pareggio!")
            break
        if turn % 2 == 0:
            print(f"{player_2} Tocca a te")
            row, column = game_move(board)
            board[row][column] = color_2
            winner = winner_evaluation(board, row, column)
        else:
            print(f"{player_1} Tocca a te")
            row, column = game_move(board)
            board[row][column] = color_1
            winner = winner_evaluation(board, row, column)
        
        turn += 1                
    
    board_printer(board)
    winner_printer(winner, color_1, color_2, player_1, player_2)

# Funzione principale che avvia il gioco

def main():
    player_1_name, player_1_color = player_1()
    player_2_name, player_2_color = player_2(player_1_color)
    color_1 = circle_color(player_1_color)
    color_2 = circle_color(player_2_color)
    board = [[" " for i in range(3)] for j in range(3)]
    engine(board, color_1, color_2, player_1_name, player_2_name)
    
if __name__ == "__main__":
    main()

