import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

genreset=set()
moviedict={}


movies11=pd.read_csv("D:/CDAC/dai2022/Day09assignment_evaluation/movies11.csv")
movies12=pd.read_csv("D:/CDAC/dai2022/Day09assignment_evaluation/movie12.csv",names=["movieId","title","genres"])
movies13=pd.read_csv("D:/CDAC/dai2022/Day09assignment_evaluation/movies13.csv",names=["movieId","title","genres"])
rating11=pd.read_excel("D:/CDAC/dai2022/Day09assignment_evaluation/rating11.xls")

moviesdata=pd.concat([movies11,movies12,movies13],ignore_index=True)

ratedf=rating11.groupby(["movieId"])["rating","timestamp"].mean()

moviesdf=pd.merge(moviesdata, ratedf, on="movieId")

moviesdf["new_gen"]=moviesdf["genres"].apply(lambda xx:str(xx).split("|"))

for gen in moviesdf["new_gen"]:
    for i in gen:
        genreset.add(i)
    
moviedict=dict.fromkeys(genreset,list())

for num , genlst in enumerate(moviesdf["new_gen"]):
    for gen in genlst:
        for keys,values in moviedict.items():
            if gen==keys:
                moviedict[gen].append(moviesdf[num][1])

        
        
        
        
        
        
        
        
        