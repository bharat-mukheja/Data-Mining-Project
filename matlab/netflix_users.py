from netflix import loadset as ld
import pandas as pd
import os
import json
import matlab.engine
from collections import defaultdict

path = 'C:\\bharat\\Work\\OneDrive - North Carolina State University\\github\\ALDA\\matlab'

os.chdir(path)

with open('user_movies_json.txt','r') as data_file:
    Users = json.load(data_file)

Users_stats = defaultdict(list)
#List format = Values returned from Matlab

eng = matlab.engine.start_matlab()
movies_df = pd.read_csv('movie_details3.csv',encoding = "ISO-8859-1")
count = 0
total = len(Users)
file_counter = 0
temp_counter = 0

def save_file(data):
    global file_counter
    file_name = 'final\\All_Users_Stats_with_p_r_'+str(file_counter)+'.txt'
    file_counter+=1
    with open(file_name, 'w') as statsfile:
        json.dump(data, statsfile)
    return


for user in Users:
    #Save temporary user movies csv in user_movie _details.csv
    try:
    #modified_df = movies_df[list(map(lambda v: v in list(map(int,Users[user])), list(movies_df.Number)))]
        df2 = pd.DataFrame(((movie, Users[user][movie]['R']) for movie in Users[user].keys()),
                           columns=['Number', 'NetflixRating'], dtype=float)
        modified_df = pd.merge(movies_df,df2,how='inner',on=['Number'])
        modified_df.to_csv('user_movie_details.csv', index=False)
        #print("saved")
        mycsvfile = ld()
        test = eng.netflix(nargout=15)
        user_prediction_stats  = list(test[:9])+[y for sublist in [x._data.tolist() for x in test[9:]] for y in sublist]
        #print(user_prediction_stats)
        Users_stats[user] = user_prediction_stats
        count+=1
    except:
        print("error")

    temp_counter+=1
    print("User done = ", user)
    print("Status = ",count,"/",total)
    break
    #if count>100:break

    if temp_counter==1000:
        save_file(Users_stats)
        Users_stats = defaultdict(list)
        temp_counter = 0

with open('final\\Rest_Users_Stats_with_p_r.txt','w') as statsfile:
    json.dump(Users_stats,statsfile)