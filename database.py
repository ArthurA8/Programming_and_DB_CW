import subscriptionManager as smSL
import feedbackManager as fmSL

# Checking Feedback Manager Works 
feedback_list = fmSL.load_feedback()
print(feedback_list)
#fmSL.add_feedback("dft01", 4, "Not bad", "Game_Feedback.txt")
print("\n")

# Checking Subscription Manager Works 
subscriptions = smSL.load_subscriptions("Subscription_Info.txt")
print(smSL.check_subscription("lbro", subscriptions)) # Should return True or False based on the current date 
print(smSL.get_rental_limit("Basic")) # Should return 2
print(smSL.get_rental_limit("Premium")) # Should return 7
