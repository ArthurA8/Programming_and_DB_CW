import subscriptionManager as smSL
import feedbackManager as fmSL
import datetime 

from datetime import datetime



# Allows a user who rented a game to return it 

def game_Return(game_ID, user_ID):

    r = open("Rental.txt", "r")

    file_lst = r.readlines()[1:]
    current_date = datetime.now().strftime("%Y-%m-%d")

    r.close()

    w = open("Rental.txt", "w")

    w.write('GameID,RentalDate,ReturnDate,RentalCustomerID,LatestReturnDate\n')

    for line in file_lst: 

        game_id = line.split(",")[0]
        rental_date = line.split(",")[1]
        return_date = line.split(",")[2]
        user_id = line.split(",")[3]
        latest_date = line.split(",")[4]

        if line.split(",")[0] == game_ID and line.split(",")[3] == user_ID and line.split(",")[2] == "N/A":
            w.write(f"{game_id},{rental_date},{current_date},{user_id},{latest_date}")

            print(f"Game successfully returned!\nRental Date: {rental_date}\nReturn Date: {current_date}\n")

        else: 
            w.write(line)
    
    w.close()
    
                 

game_Return('sna02', 'abcd')
game_Return('min01','abcd')

# Create functionality to return a message if the game was never out for rent 
# Create functionality to return a message if the game was retuned late 
# Create functionality to allow for the user to input a star rating upon return to Game_Feedback.txt
# Create functionality to allow for the user to write a review to Game_Feedback.txt
