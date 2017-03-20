# -*- coding: utf-8 -*-
import json
from csv import reader,writer,DictWriter
import requests

HEADERS = ["","Year","Title","Genre","Title","Rated","Type","imdbRating","Runtime","Director","Writer","Actors","Plot","Language","Country","Awards","Metascore","imdbVotes","imdbID"]

myreader = reader(open('C:/bharat/Work/OneDrive - North Carolina State University/CSC - 522/Project/movie_titles.txt','r'))
mywriter = writer(open('C:/bharat/Work/OneDrive - North Carolina State University/CSC - 522/Project/movie_details3.csv','w',newline=''))
mywriter.writerow(HEADERS)
rownum=0
for row in myreader:
    if rownum<10991:
        rownum+=1
        continue
    else:
        #The following part gets movie details and stores in a dictionary
        movie = row[2]
        year = row[1]
        f = json.loads(requests.get("http://www.omdbapi.com", params={'t': movie, 'y': year}).text)
        details = [row[0],year,movie]   #The dictionary which stores details useful to us.
        if f['Response'] == u'True':    #Skip adding information for Non-found movies!
            for i in HEADERS[3:]:
                details.append(f[i])
        mywriter.writerow(details)
    print('Row done='+str(row[0]))

mywriter.close()
myreader.close()
