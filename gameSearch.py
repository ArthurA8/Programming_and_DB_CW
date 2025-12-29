import subscriptionManager as smSL
import feedbackManager as fmSL

# Checks if game is video game 

def search_Vid(game_ID):
    v = open('Video_Game_Info.txt', 'r')
    for line in v: 
        ID = line.split(",")[0]
        if game_ID == ID:
            return True 
    v.close()
    return False 
    

# Checks if game is board game 

def search_Board(game_ID):
    b = open('Board_Game_Info.txt', 'r')
    for line in b:
        ID = line.split(",")[0]
        if game_ID == ID:
            return True 
    b.close()
    return False 
    

# Prints all video games 

def vid_Games():
    v = open('Video_Game_Info.txt', 'r')
    for line in v.readlines()[1:]:
        name = line.split(",")[1]
        print(name)
    v.close()

vid_Games()

# Prints all board games 

def board_Games():
    b = open('Board_Game_Info.txt', 'r')
    for line in b.readlines()[1:]:
        name = line.split(",")[1]
        print(name)
    b.close()

# Prints all video games of a specific genre 

def vid_genre(search_genre): 
    v = open('Video_Game_Info.txt', 'r')
    for line in v.readlines()[1:]:
        name = line.split(",")[1]
        genre = line.split(",")[3]
        if genre == search_genre: 
            print(name)
    v.close()

# Prints all board games of a specific genre 

def board_genre(search_genre): 
    b = open('Board_Game_Info.txt', 'r')
    for line in b.readlines()[1:]:
        name = line.split(",")[1]
        genre = line.split(",")[3]
        if genre == search_genre: 
            print(name)
    b.close()











