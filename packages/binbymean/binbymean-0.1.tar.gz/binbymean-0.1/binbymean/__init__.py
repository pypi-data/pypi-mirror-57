# -*- coding: utf-8 -*-
import pandas as pd
import array
import numpy as np
import statistics 
import collections 

def binmean():
    
    filename = str(input("Which file do you want?"))
    if not ".csv" in filename:
        filename += ".csv"
        file=pd.read_csv(filename)


    print(file.head())
    colname=input("Select Target Column for Binning: ");
    
    t=file[colname]
    targetcol=np.sort(t)
    i=0
    for x in targetcol:
        i=i+1
    
    #targetcol=np.sort(t)
    '''print(targetcol)'''
    n=i
    print("The size is ", n)

    values=[]
    uniq=[]

    number=int(input("ENTER THE NUMBER OF BINS: "))
    binsize=(int)(n/number)
    bin1=targetcol[0:binsize]
    i=1

    for j in range(2,number):
        bin=targetcol[(binsize*(j-1)+i):(binsize*j)]
        binsum=bin.sum()
        value=(int)(binsum/binsize)
        values.append(value)
        i=i+1
    

    for x in values: 
            if x not in uniq: 
                uniq.append(x)
            
    return[uniq]


    


   



            



    

