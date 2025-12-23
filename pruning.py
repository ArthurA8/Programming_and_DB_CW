import subscriptionManager as smSL
import feedbackManager as fmSL

feedback_list = fmSL.load_feedback()

# Returns list of IDs of least rented games

def least_rented():

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

    unpopular = []
    for game in freq_dict.items():
        if game[1] == min(freq_dict.values()):
            unpopular.append(game[0])

    return unpopular



# Returns game with lowest Rating 

def worst_rating():

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

    worst_rated = []

    for game in mean_ratings.items():
        if game[1] == min(mean_ratings.values()):
            worst_rated.append(game)
    
    return worst_rated
    

worst_rating()
    