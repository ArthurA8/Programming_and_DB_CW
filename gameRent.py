import subscriptionManager as smSL
import feedbackManager as fmSL
import database 
import gameSearch 

from database import is_subscribed 
from database import subscriptions 
from database import sub_type 
from database import rental_lim


# Allows user to rent game (if avaliable) and adds it to Rental.txt

def game_Rent(user_ID, game_ID, rental_Date, return_Date):
    if is_subscribed(user_ID):

        rent_db = open('Rental.txt', 'r')
        rent_lim = rental_lim(user_ID)
        num_rentals = 0

        for line in rent_db.readlines()[1:0]:
            renter_ID = line.split(",")[3]
            if renter_ID == user_ID:
                num_rentals += 1 
        
        if num_rentals == rent_lim: 
            print("Customer has reached rental limit!")
        
        elif num_rentals < rent_lim:
            pass
        # Create functionality to add game to rental.txt

    else: 
        print("Customer is not subscribed!")
    