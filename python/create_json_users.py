#This script creates a User detail json which contains the User names as keys, movie name as a dictionary value containing rating and date watched(string) as values.
#'R' = Rating, 'W' = Date of watching
#Output file = /nf_prize_dataset/download/training_set/training_set/user_movies_json.txt. Test file also placed alongside.
import pandas as pd
import json
import os
import datetime
import csv

path = 'C:\\bharat\\Work\\OneDrive - North Carolina State University\\github\\ALDA'
os.chdir(path)

movie_details = df = pd.read_csv('movie_details3.csv',encoding = "ISO-8859-1")

working_titles = list(movie_details['Number'])

path2 = 'C:\\bharat\\Work\\OneDrive - North Carolina State University\\CSC - 522\\ALDA Project\\nf_prize_dataset\\download\\training_set\\training_set'

os.chdir(path2)

Users = {}

def get_movFile_name(mov_number):
    return 'mv_'+str(mov_number).zfill(7)+'.txt.'

for i in working_titles:
    fil = csv.reader(open(get_movFile_name(i), 'r'), delimiter=',')
    next(fil)
    for row in fil:
        user_id = int(row[0])
        if user_id<100000:
            if user_id not in Users.keys(): Users[user_id]={}
            Users[user_id][str(i)] = {'R':int(row[1]),'W':row[2]}

    print('Movie done='+str(i))

for user in list(Users):
    if len(Users[user].keys())<50:
        del(Users[user])
    print("User done=",user)

print("Users Remaining = ",len(Users.keys()))

os.chdir(path)
with open('user_movies_json.txt','w+') as outfile:
    json.dump(Users,outfile)

