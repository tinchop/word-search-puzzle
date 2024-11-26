import random

print("Welcome to the Word Search Puzzle!")
print("Let's start!")


def place_word(word, empty_board):
    placed = False
    while not placed:
        pos = random.randint(0,3) #posicion: 0 horizontal, 1 vertical, 2 diagonal_der, 3 diag_izq

        if pos == 0:   #es horizontal
            row = random.randint(0, len(empty_board)-1)
            col = random.randint(0, (len(empty_board[0])-len(word)))

            reverse = random.randint(0,1)
            if reverse:
                word = word[::-1]

            aval = all(empty_board[row][col+l] in ["_", word[l]] for l in range(len(word)))
            
            if aval:
                for l in word:
                    empty_board[row][col] = word[0]
                    empty_board[row][col+1] = word[1]
                    empty_board[row][col+2] = word[2]
            placed = True
        
        elif pos == 1: #es vertical
            row = random.randint(0, (len(empty_board)-len(word)))
            col = random.randint(0, len(empty_board)-1)
            reverse = random.randint(0,1)
            if reverse:
                word = word[::-1]
            
            aval = all(empty_board[row+l][col] in ["_", word[l]] for l in range(len(word)))
            if aval:
                for l in word:
                    empty_board[row][col] = word[0]
                    empty_board[row+1][col] = word[1]
                    empty_board[row+2][col] = word[2]
            placed = True
        
        elif pos == 2: #diagonal der  
            row = random.randint(0, len(empty_board)-len(word)-1)
            col = random.randint(0, len(empty_board)-len(word)-1)

            reverse = random.randint(0,1)
            if reverse:
                word = word[::-1]

            aval = all(empty_board[row+l][col+l] in ["_", word[l]] for l in range(len(word)))
            if aval:
                empty_board[row][col] = word[0]
                empty_board[row+1][col+1] = word[1]
                empty_board[row+2][col+2] = word[2]
            placed = True

        else:
            
            row = random.randint(0+len(word), len(empty_board)-1)
            col = random.randint(0+len(word), len(empty_board)-1)

            reverse = random.randint(0,1)
            if reverse:
                word = word[::-1]

            aval = all(empty_board[row-l][col-l] in ["_", word[l]] for l in range(len(word)))
            if aval:
                empty_board[row][col] = word[0]
                empty_board[row-1][col-1] = word[1]
                empty_board[row-1][col-2] = word[2]
            placed = True      

def fill_board(empty_board, letters):
    for r in range(len(empty_board)):
        for c in range(len(empty_board)):
            if empty_board[r][c]== "_":
                empty_board[r][c]=random.choice(letters)


def create_word_search_puzzle(words_to_find):
    empty_board = [["_" for elem in range(colums)] for e in range(rows)]
    
    for word in words_to_find:
        place_word(word, empty_board) 

    fill_board(empty_board,letters)
    return empty_board
    
rows = 5
colums = 5

words_to_find = ["CAT", "DOG", "BIRD", "HAT" ,"BAT"]

letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

print("Words to find in the board below:")
random.shuffle(words_to_find)
print(words_to_find)

board = create_word_search_puzzle(words_to_find)
for f in board:
    print(*f)
