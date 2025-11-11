import sys 
sys.path.append('C:/Users/arthu/OneDrive/Desktop/Game_Store_CW/compiled_files')
sys.path.append('C:/Users/arthu/OneDrive/Desktop/Game_Store_CW/txt_DBs')
#print(sys.path)

import subscriptionManager as smSL
import feedbackManager as fmSL

feedback_list = fmSL.load_feedback()
print(feedback_list)
