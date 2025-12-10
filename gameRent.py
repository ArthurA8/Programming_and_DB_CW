import subscriptionManager as smSL
import feedbackManager as fmSL
import database 
import gameSearch 
import datetime

from database import is_subscribed 
from database import subscriptions 
from database import sub_type 
from database import rental_lim

from datetime import datetime, timedelta

from gameSearch import search_Vid, search_Board


# Allows user to rent game (if avaliable) and adds it to Rental.txt

def game_Rent(user_ID, game_ID):
    
    
    if is_subscribed(user_ID):

        if search_Vid(game_ID) or search_Board(game_ID):

            rent_db = open('Rental.txt', 'r')
            rental_Date = datetime.now().strftime("%Y-%m-%d")

            rent_lim = rental_lim(user_ID)
            year = int(rental_Date.replace('-', ' ').split()[0])
            month = int(rental_Date.replace('-', ' ').split()[1])
            day = int(rental_Date.replace('-', ' ').split()[2])

            latest_return_Date = datetime(year, month, day) + timedelta(weeks=rent_lim)
            latest_return_Date = str(latest_return_Date).replace(" 00:00:00", "")

            for line in rent_db.readlines()[1:]:
                id = line.split(',')[0]
                returned = line.split(',')[2]
                if game_ID == id and returned == 'N/A':
                    print("Failed to rent! Game is already rented!")
                    return
        
            else: 
                rent_db.close()
                write_db = open('Rental.txt', 'a')
                entry = f"{game_ID},{rental_Date},N/A,{user_ID},{latest_return_Date}"
                write_db.write(entry)
                write_db.write("\n")
                print(f"Game rented successfully! Latest return date: {latest_return_Date}")
            
        else: 
            print("Failed to rent! Game does not exist!")

    else: 
        print("Failed to rent! Customer is not subscribed!")



# Allows store manager to see what Video games are avaliable for rent

def avaliable_vid_games(): 

    r = open("Rental.txt", "r")

    unavaliable = []
    avaliable = []

    for line in r.readlines()[1:]:
        if line.split(",")[2] == "N/A":
            unavaliable.append(line)

    r.close()

    r = open("Video_Game_Info.txt", "r")

    for line in r.readlines()[1:]:
        line.replace('\n', '')
        line = line.split(",")
        line.pop(4)
        line = ','.join(line)
        avaliable.append(line)

    for entry in unavaliable:
        for line in avaliable:
            if entry.split(",")[0] == line.split(",")[0]:
                avaliable.remove(line)
    
    #print(avaliable)


#avaliable_vid_games()


# Allows store manager to see what Board games are avaliable for rent 

def avaliable_board_games(): 

    r = open("Rental.txt", "r")

    unavaliable = []
    avaliable = []

    for line in r.readlines()[1:]:
        if line.split(",")[2] == "N/A":
            unavaliable.append(line)

    r.close()

    r = open("Board_Game_Info.txt", "r")

    for line in r.readlines()[1:]:
        line.replace('\n', '')
        line = line.split(",")
        line.pop(4)
        line = ','.join(line)
        avaliable.append(line)

    for entry in unavaliable:
        for line in avaliable:
            if entry.split(",")[0] == line.split(",")[0]:
                avaliable.remove(line)
    
    print(avaliable)

#avaliable_board_games()              
