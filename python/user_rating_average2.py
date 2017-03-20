#This script generates a User mode dictionary containing the number of movies he has watched alongwith the average rating of the user.
#'Num' = Number of movies watched, 'Mode' = Mode rating
#Output file = /nf_prize_dataset/download/training_set/training_set/user_movies_modes_json.txt.

import csv
import json
import os
from collections import OrderedDict
import numpy as np
from collections import Counter

path2 = 'C:\\bharat\\Work\\OneDrive - North Carolina State University\\CSC - 522\\ALDA Project\\nf_prize_dataset\\download\\training_set\\training_set'

os.chdir(path2)

with open('user_movies_json.txt','r') as data_file:
    Users = json.load(data_file)

User_modes = OrderedDict()

total_keys = str(len(Users.keys()))
done_count = 0
max_watched = 0
min_watched = 4308

#i = user
for i in Users.keys():
    user_movies = [mov for mov in Users[i]]
    user_ratings = [Users[i][mov]["R"] for mov in Users[i]]
    num_watched = len(user_movies)
    mode_rating = Counter(user_ratings).most_common(1)[0][0]
    if num_watched>= 50:
        User_modes[i] = {'Num':num_watched,'Mode':mode_rating}
        done_count += 1
        if num_watched> max_watched: max_watched = num_watched
        if num_watched< min_watched: min_watched = num_watched
    print(str(done_count)+"/"+total_keys)
    #outfile.write(output)

with open('user_movies_modes_json.txt','w+') as outfile:
    json.dump(User_modes,outfile)

print("Max number of movies watched = "+str(max_watched))
print("Min number of movies watched = "+str(min_watched))

outfile.close()