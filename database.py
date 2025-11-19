import subscriptionManager as smSL
import feedbackManager as fmSL



#Testing functionality of compiled files 

# 1. Checking Feedback Manager Works 
feedback_list = fmSL.load_feedback()
#print(feedback_list)
#fmSL.add_feedback("dft01", 4, "Not bad", "Game_Feedback.txt")
#print("\n")

# 2. Checking Subscription Manager Works 
#print(smSL.check_subscription("lbro", subscriptions)) # Should return True or False based on the current date 
#print(smSL.get_rental_limit("Basic")) # Should return 2
#print(smSL.get_rental_limit("Premium")) # Should return 7


# Use to check for a subscription 

def is_subscribed(user_id):
    subscriptions = smSL.load_subscriptions()
    subscribed = smSL.check_subscription(user_id, subscriptions)
    return subscribed

# Access subscriptions as a dictionary 

def subscriptions(): 
    return smSL.load_subscriptions()


# Check subscription type:

def sub_type(user_id): 
    sub_dict = smSL.load_subscriptions()
    user_info = sub_dict[f'{user_id}']
    if user_info['SubscriptionType'] == 'Premium':
        return 'Premium'
    elif user_info['SubscriptionType'] == 'Basic':
        return 'Basic'
    
# Returns rental time limit:

def rental_lim(user_id):
    if sub_type(user_id) == 'Premium':
        return 7 
    elif sub_type(user_id) == 'Basic':
        return 2 

# Removes game from respective txt DB 

def remove_game(game_id, db_name):
    with open(f'{db_name}', 'r') as r:
        file_lst = r.readlines()[1:]
        with open(f'{db_name}', 'w') as w:
            w.write('GameID,Name,Platform,Genre,PurchaseDate\n')
            for line in file_lst:
                id = line.split(",")[0]
                if game_id != id: 
                    w.write(line)


                    




