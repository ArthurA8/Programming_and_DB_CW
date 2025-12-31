import subscriptionManager as smSL
import feedbackManager as fmSL
import matplotlib.pyplot as plt

feedback_list = fmSL.load_feedback()




# Returns a dictionary of games and their rental frequency

def all_rentings():

    r = open("Rental.txt", "r")

    freq_dict = {}
    
    for line in r.readlines()[1:]:
        game_id = line.split(",")[0]
        
        if freq_dict.get(game_id) == True:
            freq_dict[game_id] += 1

        elif freq_dict.get(game_id) == None:
            freq_dict[game_id] = 1 
    
    r.close()

    r = open("Video_Game_Info.txt")

    for line in r.readlines()[1:]:
        game_id = line.split(",")[0]

        if freq_dict.get(game_id) == None:
            freq_dict[game_id] = 0
    
    r.close()

    r = open("Board_Game_Info.txt")

    for line in r.readlines()[1:]:
        game_id = line.split(",")[0]

        if freq_dict.get(game_id) == None:
            freq_dict[game_id] = 0
    
    r.close()

    return(freq_dict)




# Returns a dictionary of games and their mean rating 

def average_ratings():
    rated_games = []

    for game in feedback_list:
        if game['GameID'] in rated_games:
            pass 
        else:
            rated_games.append((game['GameID'], []))


    for game in rated_games:
        for review in feedback_list:
            if review['GameID'] == game[0]:
                game[1].append(review['Rating'])

    mean_ratings = {}           
    
    for game in rated_games:

        summed = 0
        for rating in game[1]:
            summed += rating 

        mean = summed / len(game[1])

        mean_ratings[game[0]] = mean
    
    return mean_ratings



# Returns list of IDs of least rented games

def least_rented():

    freq_dict = all_rentings()

    unpopular = []
    for game in freq_dict.items():
        if game[1] == min(freq_dict.values()):
            unpopular.append(game[0])

    return unpopular



# Returns game with lowest Rating 

def worst_rating():

    mean_ratings = average_ratings()

    worst_rated = []

    for game in mean_ratings.items():
        if game[1] == min(mean_ratings.values()):
            worst_rated.append(game)
    
    return worst_rated
   


# Function to find name of a game from its ID

def id_to_name(id):
    
    v = open("Video_Game_Info.txt", "r")
    b = open("Board_Game_Info.txt", "r")

    game_names = []

    for line in v.readlines()[1:]:
        game_id = line.split(",")[0]
        game_name = line.split(",")[1]
        game_names.append((game_id, game_name))
    
    for line in b.readlines()[1:]:
        game_id = line.split(",")[0]
        game_name = line.split(",")[1]
        game_names.append((game_id, game_name))
    
    v.close()
    b.close()

    for entry in game_names:
        if entry[0] == id:
            return entry[1]




# Defining Bar Chart analytics

def plot(type):

    with analytics_output:

        game_ids = []

        r = open("Video_Game_Info.txt", "r")
        for line in r.readlines()[1:]:
            game_id = line.split(",")[0]
            game_ids.append(game_id)
        r.close()

        r = open("Board_Game_Info.txt", "r")
        for line in r.readlines()[1:]:
            game_id = line.split(",")[0]
            game_ids.append(game_id)
        r.close()

        if type == "frequency":

                plt.close('all')
                x = []
                y = []

                for entry in all_rentings().items():
                    if entry[0] in game_ids:
                        x.append(entry[0])
                        y.append(entry[1])

                plt.figure(figsize=(4, 3))
                plt.bar(x, y)
                plt.xlabel("Game ID")
                plt.ylabel("Rental Freq")
                plt.ylim(0, 10)
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.show()


        if type == "rating":

                plt.close('all')
                x = []
                y = []

                for entry in average_ratings().items():
                    if entry[0] in game_ids:
                        x.append(entry[0])
                        y.append(entry[1])

                plt.figure(figsize=(4, 3))
                plt.bar(x, y)
                plt.xlabel("Game ID")
                plt.ylabel("Mean Rating")
                plt.ylim(0, 5)
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.show()

