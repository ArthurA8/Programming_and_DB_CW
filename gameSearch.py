import subscriptionManager as smSL
import feedbackManager as fmSL

v = open('Video_Game_Info.txt', 'r')
b = open('Board_Game_Info.txt', 'r')

# Checks if game is video game 

def search_Vid(game_ID):
    for line in v: 
        ID = line.split(",")[0]
        if game_ID == ID:
            return True 
    return False 
    v.close()

# Checks if game is board game 

def search_Board(game_ID):
    for line in b:
        ID = line.split(",")[0]
        if game_ID == ID:
            return True 
    return False 
    b.close()

# Prints all video games 

def vid_Games():
    for line in v.readlines()[1:]:
        name = line.split(",")[1]
        print(name)

# Prints all board games 

def board_Games():
    for line in b.readlines()[1:]:
        name = line.split(",")[1]
        print(name)

# Prints all video games of a specific genre 

def vid_genre(search_genre): 
    for line in v.readlines()[1:]:
        name = line.split(",")[1]
        genre = line.split(",")[3]
        if genre == search_genre: 
            print(name)

# Prints all board games of a specific genre 

def board_genre(search_genre): 
    for line in b.readlines()[1:]:
        name = line.split(",")[1]
        genre = line.split(",")[3]
        if genre == search_genre: 
            print(name)











