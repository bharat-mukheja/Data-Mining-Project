##This script converts parses the JSON details of User details and outputs a much simpler json with only Usernames and Movie names for easy referencing and calculations.
#Output file = /nf_prize_dataset/download/training_set/training_set/user_movies_names_json.txt.

import csv
import json
import os
from collections import OrderedDict

path2 = 'C:\\bharat\\Work\\OneDrive - North Carolina State University\\github\\ALDA'

os.chdir(path2)

with open('user_movies_json.txt','r') as data_file:
    Users = json.load(data_file)

Users_movies = OrderedDict()

total_keys = str(len(Users.keys()))
done_count = 0

for i in Users.keys():
    Users_movies[i] = [mov for mov in Users[i].keys()]
    #print(Users_movies[i])
    done_count+=1
    print(str(done_count)+"/"+total_keys)
    #outfile.write(output)

with open('user_movies_names_json.txt','w+') as outfile:
    json.dump(Users_movies,outfile)

outfile.close()