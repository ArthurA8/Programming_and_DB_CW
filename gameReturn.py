import subscriptionManager as smSL
import feedbackManager as fmSL
import datetime 

from datetime import datetime

return_status = None

# Allows a user who rented a game to return it 


def game_Return(game_ID, user_ID):

    global return_status

    rental_logs = []

    r = open("Rental.txt", "r")

    for line in r.readlines()[1:]:

        rental_logs.append(line.replace("\n", ""))

    return_history = []

    for line in rental_logs:
        if line.split(",")[0] == game_ID:
            return_history.append(line.split(",")[2])

    
    r.close()

    if "N/A" in return_history:

        w = open("Rental.txt", "w")
        w.write("GameID,RentalDate,ReturnDate,RentalCustomerID,LatestReturnDate")

        for line in rental_logs: 

            game_id = line.split(",")[0]
            rental_date = line.split(",")[1]
            return_date = line.split(",")[2]
            user_id = line.split(",")[3]
            latest_date = line.split(",")[4]
            current_date = datetime.now().strftime("%Y-%m-%d")
            concat_latest_date = int(latest_date.replace("-", ""))
            concat_return_date = int(current_date.replace("-", ""))

            if all([game_id == game_ID, user_id == user_ID, return_date == "N/A"]):

                w.write(f"\n{game_id},{rental_date},{current_date},{user_id},{latest_date}")

                if concat_return_date > concat_latest_date: 
                    return_status = "Late"

                elif concat_return_date < concat_latest_date: 
                    return_status = "On Time"            

            else: 
                w.write(f"\n{line}")
    
        w.close()
    
    else:
        return_status = "Invalid"



    


game_Return("min01", "abcd")





