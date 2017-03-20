import csv
from collections import defaultdict
from math import ceil

def list_into_set(setname,listname,imdbrating,countset):
    li=listname.split(', ')
    for item in li:
        countset[item]=countset[item]+1
        setname[item]=int(imdbrating)+setname[item]
    return 

def avg_col_val(setname,listname):
    li=listname.split(', ')
    i=0
    avg_ans=0
    for item in li:
        i=i+1
        avg_ans=avg_ans+setname[item]

    avg_ans=avg_ans/float(i)
    return avg_ans
    
def avg_set(setname,countset):
    for k, v in setname.items():
        if countset[k] != 0:
            setname[k]=setname[k]/countset[k]
    #print setname
    

def loadset():    
    reader = csv.reader(open('user_movie_details.csv', 'r'))
    genre_set=defaultdict(lambda: 0)
    genre_count=defaultdict(lambda: 0)
    
    Rated_set=defaultdict(lambda: 0)
    Rated_count=defaultdict(lambda: 0)
    
    Type_set=defaultdict(lambda: 0)
    Type_count=defaultdict(lambda: 0)
    
    Director_set=defaultdict(lambda: 0)
    Director_count=defaultdict(lambda: 0)
    
    Writer_set=defaultdict(lambda: 0)
    Writer_count=defaultdict(lambda: 0)
    
    Actors_set=defaultdict(lambda: 0)
    Actors_count=defaultdict(lambda: 0)
    
    Language_set=defaultdict(lambda: 0)
    Language_count=defaultdict(lambda: 0)
    
    Country_set=defaultdict(lambda: 0)
    Country_count=defaultdict(lambda: 0)
    for count,row in enumerate(reader):
       Number,Year,Title,Genre,Rated,Type,imdbRating,Runtime,Director,Writer,Actors,Language,Country,Awards,imdbVotes,imdbID,NetflixRating= row
       if count >0:
           imdbceil=ceil(float(imdbRating))    
           Type_set[Type]=imdbceil+Type_set[Rated]
           Type_count[Type]=Rated_count[Type]+1
           Rated_set[Rated]=imdbceil+Rated_set[Rated]
           Rated_count[Rated]=Rated_count[Rated]+1      
           list_into_set(genre_set, Genre,imdbceil,genre_count)           
           Director_set[Director]=imdbceil+Director_set[Director]
           Director_count[Director]=1+Director_count[Director]
           list_into_set(Writer_set,Writer,imdbceil,Writer_count)
           list_into_set(Actors_set,Actors,imdbceil,Actors_count)
           list_into_set(Language_set, Language,imdbceil,Language_count)
           list_into_set(Country_set,Country,imdbceil,Country_count)
    
    avg_set(Type_set,Type_count)
    avg_set(Rated_set, Rated_count)
    avg_set(genre_set,genre_count)    
    avg_set(Director_set, Director_count)
    avg_set(Writer_set, Writer_count)
    avg_set(Actors_set,Actors_count)
    avg_set(Language_set, Language_count)
    avg_set(Country_set, Country_count)
    #print genre_set
    #print Rated_set
    #print Type_set  
    #print Writer_set
    #print Actors_set
    #print Language_set
    #print Country_set
    #print Director_set.__len__()
    
            
    
    reader = csv.reader(open('user_movie_details.csv', 'r'))
    with open('user_Transformed.csv', 'w',newline='') as mycsvfile:
        thedatawriter = csv.writer(mycsvfile)
        for count,row in enumerate(reader):
            Number,Year,Title,Genre,Rated,Type,imdbRating,Runtime,Director,Writer,Actors,Language,Country,Awards,imdbVotes,imdbID,NetflixRating = row
            if count >0 :
                imdbceil=ceil(float(imdbRating))    
                Awards_sum=sum([int(s) for s in Awards.split() if s.isdigit()])
                Runtime_strip=sum([int(s) for s in Runtime.split() if s.isdigit()])
                
                avg_gen=avg_col_val(genre_set, Genre)
                avg_actor=avg_col_val(Actors_set, Actors)
                avg_con=avg_col_val(Country_set, Country)
                avg_lan=avg_col_val(Language_set,Language)
                avg_writer=avg_col_val(Writer_set, Writer)
                new_row=Number,Year,Title,avg_gen,Rated_set[Rated],Type_set[Type],Runtime_strip,Director_set[Director],avg_writer,avg_actor,avg_lan,avg_con,Awards_sum,imdbceil,NetflixRating
                thedatawriter.writerow(new_row)
            else:
                thedatawriter.writerow([Number,Year,Title,Genre,Rated,Type,Runtime,Director,Writer,Actors,Language,Country,Awards,imdbRating,NetflixRating])
            
    #print Director_set['Mike van Diem']
    #print genre_set
   
    return

    


loadset()

