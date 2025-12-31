import subscriptionManager as smSL
import datetime
from database import is_subscribed
from datetime import datetime, timedelta

# Function checking avaliability of day and time slot 

def avaliability(date, time_slot): 

  

    r = open("Booking.txt", "r")
    selected_date = date.strftime("%Y-%m-%d")

    slot_data = []
    for line in r.readlines()[1:]:
        if line.split(",")[1] == selected_date and line.split(",")[2] == time_slot:
            slot_data.append(int(line.split(",")[3]) + 1)
        
    num_ppl = sum(slot_data)
    r.close()

    return (num_ppl, 50 - num_ppl)
 

# Function adding new entry to Booking.txt 

def booking(user_ID, date, time_slot, No_Guests):

    r = open("Booking.txt", "r")
    logs = r.readlines()[1:]
    r.close()

    for line in logs:
        if line.split(",")[0] == user_ID and line.split(",")[1] == date and line.split(",")[2] == time_slot:
            return "invalid"
    
    a = open("Booking.txt", "a")
    a.write(f"\n{user_ID},{date},{time_slot},{No_Guests}")
    return "success"


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
    
