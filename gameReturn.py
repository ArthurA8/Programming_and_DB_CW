import subscriptionManager as smSL
import feedbackManager as fmSL
import datetime 

from datetime import datetime



# Allows a user who rented a game to return it 

def game_Return(game_ID, user_ID):

    # Creating a list containing Rental.txt entries: 

    r = open("Rental.txt", "r")
    file_lst = r.readlines()[1:]
    r.close()

    # Fetching and formatting current date for return date:

    current_date = datetime.now().strftime("%Y-%m-%d")

    # Creating a list containing Return history for the specified game:

    game_return_history = []
    for line in file_lst:
        if line.split(",")[0] == game_ID:
            game_return_history.append(line.split(",")[2])

    # Checking to see if the game was out for return:
    
    if "N/A" in game_return_history:

        # Rewriting Rental.txt to fill return date entry:

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

                concat_latest_date = int(latest_date.replace("-", ""))
                concat_return_date = int(current_date.replace("-", ""))

                # Once returned, checking to see if the game was returned late:
                
                if concat_return_date > concat_latest_date: 
                    print(f"Customer has returned the game late!\nReturn Date: {current_date}\nLatest Return Date: {latest_date}")

            else: 
                w.write(line)
    
        w.close()

        # Adding rating and comment to Game_Feedback.txt upon return:

        # Use radio buttons or something in the GUI to ensure only 1-5 can be inputted
        rating = int(input("Please enter a star rating 1-5: "))
        comments = str(input("Please enter a short comment on the game: "))

        w = open("Game_Feedback.txt", "a")
        w.write(f'\n{game_ID},{rating},{comments}')

        print("Rating and comment submitted!")

        w.close()

    
    else: 
        print("Game is not out for return!")
    
                 

game_Return('sna02', 'abcd')



