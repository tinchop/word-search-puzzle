import random

print("Welcome to the Word Search Puzzle!")
print("Let's start!")

def is_space_available(word, empty_board, row, col, direction):  
    if direction == 0: 
        if col + len(word) > len(empty_board[0]): 
            return False
        else:
            for l in range(len(word)):
                if empty_board[row][col + l] not in ["_", word[l]]:
                    return False
    
    elif direction == 1:  
        if row + len(word) > len(empty_board): 
            return False
        else:
            for l in range(len(word)):
                if empty_board[row + l][col] not in ["_", word[l]]:
                    return False
    
    elif direction == 2:  
        if row + len(word) > len(empty_board) or col + len(word) > len(empty_board[0]):
            return False
        else:
            for l in range(len(word)):
                if empty_board[row + l][col + l] not in ["_", word[l]]:
                    return False
    
    else:  
        if row - len(word) < -1 or col - len(word) < -1:
            return False
        else:
            for l in range(len(word)):
                if empty_board[row - l][col - l] not in ["_", word[l]]:
                    return False
    
    return True

def place_word(word, empty_board):
    placed = False
    max_attempts = 100
    attempts = 0
    while not placed and attempts < max_attempts:
        reverse = random.randint(0, 1)
        if reverse:
            word = word[::-1]

        pos = random.randint(0, 3)  # 0 horizontal, 1 vertical, 2 diag_right, 3 diag_left
        #position
        if pos == 0:  # horizontal
            row = random.randint(0, len(empty_board) - 1)
            col = random.randint(0, len(empty_board[0]) - len(word))
        
        elif pos == 1:  # Vertical
            row = random.randint(0, len(empty_board) - len(word))
            col = random.randint(0, len(empty_board[0]) - 1)
        
        elif pos == 2:  #diag_right
            row = random.randint(0, len(empty_board) - len(word))
            col = random.randint(0, len(empty_board[0]) - len(word))
        
        else:  # diag_left
            row = random.randint(len(word) - 1, len(empty_board) - 1)
            col = random.randint(len(word) - 1, len(empty_board[0]) - 1)

        if is_space_available(word, empty_board, row, col, pos):
            if pos == 0:  
                for l in range(len(word)):
                    empty_board[row][col + l] = word[l]
            elif pos == 1:  
                for l in range(len(word)):
                    empty_board[row + l][col] = word[l]
            elif pos == 2:  
                for l in range(len(word)):
                    empty_board[row + l][col + l] = word[l]
            else:  
                for l in range(len(word)):
                    empty_board[row - l][col - l] = word[l]
            placed = True
        
        attempts += 1

    if not placed:
        print(f"Words out of board: {word}")


def fill_board(empty_board, letters):
    for r in range(len(empty_board)):
        for c in range(len(empty_board[0])):
            if empty_board[r][c] == "_":
                empty_board[r][c] = random.choice(letters)


def create_word_search_puzzle(words_to_find):
    empty_board = [["_" for _ in range(columns)] for _ in range(rows)]
    
    for word in words_to_find:
        place_word(word, empty_board) 

    fill_board(empty_board, letters)
    return empty_board
    
rows, columns = 5, 5

words_to_find = ["CAT", "DOG", "BIRD", "HAT", "BAT"]

letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

print("Words to find in the board below:")
random.shuffle(words_to_find)
print(words_to_find)

board = create_word_search_puzzle(words_to_find)
for row in board:
    print(" ".join(row))
