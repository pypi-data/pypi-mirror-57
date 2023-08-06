# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 04:16:54 2019

@author: sachinthakur9614
"""


from scipy import stats
import itertools
import pandas as pd

import numpy as np
#import matplotlib.pyplot as plt





def bin_by_median(filepath,column,numrows,bin_num):
    

    df = pd.read_csv(filepath)
    
    
    saved_column = df[column]
    
    
    
    row_no = numrows
    id1 = 0
    list_col = []
    
    for row in itertools.islice(saved_column,0,row_no):
        list_col.append(row)
        print(id1," ",row)
        id1+=1;
    array = np.array(list_col)
    print(array)
    print(" ")
    array = np.sort(array)
    print(" The Sorted array is:")
    print(array)
    
    
    for i in range(1,bin_num):
        
    
        bin_1 = []
        bin_2 = []
        bin_3 = []
        # array.sort()
        
        
        if (len(array)%bin_num != 0):
            print("Invalid Bin Number")
        bins = np.split(array,bin_num)
        print(bins)
        
        print("total number of bins",bins)
        bin_1=[]
        for i in range(0,bin_num):
            
            med1 = 0
            med1 = np.median(bins[i])
            bin_2=[]
            for x in bins[i]:
                
                bin_2.append(med1)
            #print("bin data is,",i,":",bin_1[i])
            bin_1.append(bin_2[0])
        
        return bin_1
          






