import subscriptionManager as smSL
import datetime
from database import is_subscribed
from datetime import datetime, timedelta

def booking(user_ID, time_slot): 

    if is_subscribed(user_ID) == True: 
        pass 

    else: 
        return "Not Subscribed"


# Function which checks if inputted date is within 1 week of current date:

def within_a_week(date):

    selected_date = date.strftime("%Y-%m-%d")
    current_date = datetime.now().strftime("%Y-%m-%d")

    year = int(current_date.replace('-', ' ').split()[0])
    month = int(current_date.replace('-', ' ').split()[1])
    day = int(current_date.replace('-', ' ').split()[2])

    week_time = datetime(year, month, day) + timedelta(weeks=1)
    week_time = str(week_time).replace(" 00:00:00", "")

    concat_week_time = int(week_time.replace("-", ""))
    concat_selected_date = int(selected_date.replace("-", ""))
    concat_current_date = int(current_date.replace("-", ""))

    if concat_week_time < concat_selected_date: 
        return False 
    
    elif concat_selected_date < concat_current_date: 
        return False
    
    else:
        return True
    
