# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 10:24:04 2021

@author: Pei Ren
"""


import pandas as pd 
import numpy as np



pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

df = pd.DataFrame(index=list(range(1,101)), columns = ["Student ID"]) 
df["Student ID"] = list(range(2001001,2001101))
df["Maths"] = np.random.randint(40,101, size=100)
df["Physics"] = np.random.randint(35,101, size=100)
df["Chemistry"] = np.random.randint(50,101, size=100)
df["Biology"] = np.random.randint(40,91, size=100)
df["English"] = np.random.randint(60,86, size=100)

Mylist = list(df)
Mylist.remove ("Student ID")
df["Total"] = df[Mylist].sum(axis = 1)
df["Average"] = df[Mylist].sum(axis = 1)/ len(Mylist)

Totalmarks = df["Total"].sum(axis = 0)

Count = sum(df[Mylist].count(axis = 0))

Totalaverage = Totalmarks/ Count

df.loc[df["Average"] >= Totalaverage, "Overall"] = 1
df.loc[df["Average"] < Totalaverage, "Overall"] = 2
df["Overall"] = df["Overall"].apply(np.int64)


print(df)
print ("Total marks is =" , Totalmarks)
print ("Total count is =", Count)
print("Total average is =", Totalaverage)



#for loop answer

# create a random table (qns 3 of assignment)

# import numpy as np
# # Initialise a 100 by 9 null matrix to be filled with data
# ClassList = np.zeros((100,9))
# # Fills the first column with numbers 1 to 100
# ClassList[:,0]=range(1,101)
# # First for loop to generate random integer values as marks
# for i in range(0,100):

#     ClassList[i,1]= np.random.randint(40,101)
#     ClassList[i,2]= np.random.randint(35,101)
#     ClassList[i,3]= np.random.randint(50,101)
#     ClassList[i,4]= np.random.randint(40,91)
#     ClassList[i,5]= np.random.randint(60,86)
# # Calculates the sum of columns 2 through 5 and fills column 6 with this value
#     ClassList[i,6]=np.sum(ClassList[i,1:6])
# # Calculates the average of columns 2 through 5 and fills column 6 with this value
#     ClassList[i,7]=np.average(ClassList[i,1:6])
# # Calculates the average of all the rows in column 6 as the class average
# ClassAverage=np.average(ClassList[:,7])
# # Second for loop to check conditional statement
# for i in range(0,100):
#     ClassList[i,8] = 1 if ClassList[i,7] >= ClassAverage else 2
# # Prints completed ClassList
# print(ClassList)
# print('Average Class Score:', ClassAverage)
