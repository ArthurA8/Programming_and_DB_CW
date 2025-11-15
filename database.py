import subscriptionManager as smSL
import feedbackManager as fmSL



#Testing functionality of compiled files 

# 1. Checking Feedback Manager Works 
feedback_list = fmSL.load_feedback()
#print(feedback_list)
#fmSL.add_feedback("dft01", 4, "Not bad", "Game_Feedback.txt")
#print("\n")

# 2. Checking Subscription Manager Works 
subscriptions = smSL.load_subscriptions()
#print(smSL.check_subscription("lbro", subscriptions)) # Should return True or False based on the current date 
#print(smSL.get_rental_limit("Basic")) # Should return 2
#print(smSL.get_rental_limit("Premium")) # Should return 7


# Use to check for a subscription 

def is_subscribed(user_id):
    return smSL.check_subscription(f"{user_id}", subscriptions)

# Access subscriptions as a dictionary 

def subscriptions(): 
    return smSL.load_subscriptions()

print(subscriptions())

# Check subscription type:

def sub_type(user_id): 
    sub_dict = smSL.load_subscriptions()
    user_info = sub_dict[f'{user_id}']
    if user_info['SubscriptionType'] == 'Premium':
        return 'Premiun'
    elif user_info['SubscriptionType'] == 'Basic':
        return 'Basic'



