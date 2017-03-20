#This script creates a txt file with comma separated movie names for each user in sample.
#Output file = /nf_prize_dataset/download/training_set/training_set/user_movies.txt. Test file also placed alongside.
import csv
import json
import os

path2 = 'C:\\bharat\\Work\\OneDrive - North Carolina State University\\CSC - 522\\ALDA Project\\nf_prize_dataset\\download\\training_set\\training_set'

os.chdir(path2)

with open('user_movies_json.txt','r') as data_file:
    Users = json.load(data_file)

outfile = open('user_movies.txt','w')

total_keys = str(len(Users.keys()))
done_count = 0

for i in Users.keys():
    output = str(i) + " = " + ", ".join([str(mov) for mov in Users[i].keys()])+"\n"
    #print(output)
    done_count+=1
    print(str(done_count)+"/"+total_keys)
    outfile.write(output)

outfile.close()