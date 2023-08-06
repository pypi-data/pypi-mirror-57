# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 09:46:53 2019

@author: Vikash
"""

# -*- coding: utf-8 -*-
import pandas as pd
import array
import itertools
import numpy as np
import statistics

def bin():
   
    filename = str(input("Which file do you want?"))
    if not ".csv" in filename:
        filename += ".csv"
        file=pd.read_csv(filename)


    print("COLUMN NAMES \n")
    l=file.columns.values
    c=0
    for i in file:
        c=c+1
        print(c, "-" , i)

    colname=int(input("ENTER ID OF COLUMN :"))
    print("YOU HAVE SELECTED COLUMN :",l[colname-1])
    targetcol=file[l[colname-1]]
    n=targetcol.count()
    print("NUMBER OF DATA", n)
    
    if type(targetcol.iloc[0]) == str:
        print("THIS FUNCTION CAN BE APPLIED ON INTEGER TYPE ONLY ")
        return
    
    row_no = n
    id1 = 0
    list_col = []
    

    for row in itertools.islice(targetcol,0,row_no):
        list_col.append(row)
        id1+=1;
    array = np.array(list_col)

    array = np.sort(array)
    print("THE SORTED ARRAY IS:")
    print(array)   
    
    number=int(input("ENTER THE NUMBER OF BINS:"))
    bin_num=number
    binsize=(int)(n/bin_num)
    bin1=array[0:n]
    i=1
    
 
        
    if (len(array)%bin_num != 0):
           print("Invalid Bin Number")
           
    bins = np.split(array,bin_num)

        
    print("TOTAL NUMBER OF BINS :\n\n\n",bins,"\n")
    print("VALUE OF BIN BY BOUNDARY(Min-Max):",number)
    for j in range(1,number+1):
             bin=bin1[(binsize*(j-1)):(binsize*j)]
             binmin=bin.min()
             binmax=bin.max()
             print("Bin",j,":","[",binmin,",",binmax,"]")
             

             
print(bin())
