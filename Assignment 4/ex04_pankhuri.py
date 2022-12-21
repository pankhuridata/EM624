#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import csv
from datetime import datetime
import time
from operator import itemgetter


# In[2]:


with open('JC-201611-citibike-tripdata.csv', newline='') as file1:    # Reading both files and converting csv to list
    reader = csv.reader(file1)
    citi = list(reader)

with open('JC-202111-citibike-tripdata.csv', newline='') as file2:
    reader = csv.reader(file2)
    bike = list(reader)


# In[3]:


df_citi = pd.DataFrame(citi)                          # merging the files and printing the data
df_bike = pd.DataFrame(bike)
df_merged = [df_citi, df_bike]
print("\n", df_merged)


# In[4]:


c_list = df_citi.values.tolist() #Converting to list of lists
b_list = df_bike.values.tolist() 


# In[5]:


def print_bike_details():
    start_time = []
    end_time = []
    start_station = []
    end_station = []
    time_difference = []
    
    for i in range(1,len(b_list)):
        start_time.append(b_list[i][2])
        end_time.append(b_list[i][3])
        start_station.append(b_list[i][4])
        end_station.append(b_list[i][6])
    
    for i in range(len(start_time)): 
        tD = (datetime.strptime(end_time[i],'%Y-%m-%d %H:%M:%S'))-(datetime.strptime(start_time[i],'%Y-%m-%d %H:%M:%S'))
        time_difference.append(tD.total_seconds())
        
    print('\nAverage Duration Time = ', sum(time_difference)/len(time_difference), 'secs')

    starting_counter = 0
    ending_counter = 0
    member_counter = 0
    casual_counter = 0
    for i in range(1, len(b_list)):
        if b_list[i][12] == 'member': member_counter += 1
        else: casual_counter += 1
    
        if b_list[i][4] != '': starting_counter += 1
        if b_list[i][6] != '': ending_counter += 1
            
    print('\nNo.of times Starting Station used = ', starting_counter, '\nNo.of times Ending Station is used = ', ending_counter)
    
    start_dict = {i:start_station.count(i) for i in start_station}
    top_5 = dict(sorted(start_dict.items(), key = itemgetter(1), reverse = True)[:5])
    print('\nThe five most populat starting stations are \n'+str(top_5))
    
    end_dict = {i:end_station.count(i) for i in end_station}
    top_5 = dict(sorted(end_dict.items(), key = itemgetter(1), reverse = True)[:5])
    print('\nThe five most populat ending stations are \n'+str(top_5))
    
    print('\nNo.of Memebers = ',member_counter,'\nNo.of Casuals = ', casual_counter)
    
    return


# In[6]:


print_bike_details()


# In[ ]:




