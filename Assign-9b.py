import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

movies11=pd.read_csv("D:/CDAC/dai2022/Day09assignment/movies11.csv")
movies12=pd.read_csv("D:/CDAC/dai2022/Day09assignment/movie12.csv",names=["movieId","title","genres"])
movies13=pd.read_csv("D:/CDAC/dai2022/Day09assignment/movies13.csv",names=["movieId","title","genres"])
rating11=pd.read_excel("D:/CDAC/dai2022/Day09assignment/rating11.xls")

moviesdata=pd.concat([movies11,movies12,movies13],ignore_index=True)


# to create movie[keys] and new_gen[value] dictonary in moivesdata df
genset1=set()
tempdict1=dict() 
tempdict2=dict()
tempdict3=dict()

######################################################################
""" without rating file merge"""

moviesdata["new_gen"]=moviesdata["genres"].apply(lambda xx:str(xx).split("|"))

for title,genlist in zip(moviesdata["title"],moviesdata["new_gen"]):
    tempdict1[title]=genlist

for title,genlist in tempdict1.items():
    
    for i in genlist:
        genset1.add(i)
        if i not in tempdict2.keys():
            tempdict2[i]=set()
            tempdict2[i].add(title)
        else:
            tempdict2[i].add(title)

######################################################################
'''
###Q-1. find all masala movie - (action ,romance,comedy,thriller)

genlist1=list(genset1)
genlist1.sort()
for num,gen in enumerate(genlist1,1):
    tempdict3[num]=gen

ans="y"

movieset1=set()
print("Enter choice of genres to find movies:")
for num,gen in tempdict3.items():
    print(f"{num}: {gen} ",end="\t")

while ans=="y" or ans=="Y":
    choice=int(input("\nChoice: "))
    gen=tempdict3[choice]
    movie=tempdict2[gen]
    for i in movie:
        movieset1.add(i)
    ans=input("want to add more?(y/n): ")

print("The movies are: ")
for num,movie in enumerate(movieset1,1):
    print(f"{num}: {movie}")
'''
######################################################################
'''
###Q-2. plot a pie chart to represent genre and frequency of movie count

gen_name=[]
gen_count=[]

for gen,movie in tempdict2.items():
    gen_name.append(gen)
    gen_count.append(len(movie))

fig = plt.figure(figsize =(10,15))
plt.pie(gen_count,labels=gen_name,autopct="%1.2f%%",startangle=90)
plt.show()
'''
######################################################################

###Q-3. average rating for each movie(using movieid  in rating csv) and merge 2 frames

# to create movie[keys] and new_gen[value] dictonary in moivesdf
genset2=set()
tempdict4=dict()
tempdict5=dict()

ratedf=rating11.groupby(["movieId"])["rating","timestamp"].mean()

moviesdf=pd.merge(moviesdata, ratedf, on="movieId")

""" with rating file merge"""

for title,genlist in zip(moviesdf["title"],moviesdf["new_gen"]):
    tempdict4[title]=genlist

for title,genlist in tempdict4.items():
    for i in genlist:
        genset2.add(i)
        if i not in tempdict5.keys():
            tempdict5[i]=set()
            tempdict5[i].add(title)
        else:
            tempdict5[i].add(title)

######################################################################

###Q-4. draw pie chart for each genre and average rating

#to create relation between rating and genre
genset3=set()
tempdict6=dict()
tempdict7=dict()

moviesdf['rating']=round(moviesdf['rating'],2)
moviesdf['timestamp']=moviesdf['timestamp'].astype("int")

for rating,genlist in zip(moviesdf["rating"],moviesdf["new_gen"]):
    genset3=set(genlist)
    if rating not in tempdict6.keys():
        tempdict6[rating]=set()
        for x in genset3:
            tempdict6[rating].add(x)
    else:
        for x in genset3:
            tempdict6[rating].add(x)

for rating,genlist in tempdict6.items():
    for i in genlist:
        if i not in tempdict7.keys():
            tempdict7[i]=list()
            tempdict7[i].append(rating)
        else:
            tempdict7[i].append(rating)

gen_list=[]
gen_mean=[]

for gen,rating in tempdict7.items():
    gen_list.append(gen)
    genm=round(np.mean(rating),2)
    gen_mean.append(genm)

fig = plt.figure(figsize =(10,15))
plt.pie(gen_mean,labels=gen_list,autopct="%1.2f%%",startangle=90)
plt.show()

######################################################################

###Q-5. draw bar graph for each rating and number of movies

def ratingsort(rating):
    if rating>4.5:
        return 5
    elif 4.5>=rating>3.5:
        return 4
    elif 3.5>=rating>2.5:
        return 3
    elif 2.5>=rating>1.5:
        return 2
    else:
        return 1
    
rate_movie=dict()

for movie, rating in zip(moviesdf["title"],moviesdf["rating"]):
    rate=ratingsort(rating)
    if rate not in rate_movie.keys():
        rate_movie[rate]=list()
        rate_movie[rate].append(movie)
    else:
        rate_movie[rate].append(movie)

rate_m=list()
movie_c=list()

for rate,movie in rate_movie.items():
    rate_m.append(rate)
    count=len(movie)
    movie_c.append(count)

fig = plt.figure(figsize =(10,15))
plt.bar(rate_m, movie_c,color=("red","blue","pink","green","yellow"))
plt.show()
