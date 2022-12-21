"""
Author ----
Date ----

EMx24 Exercise 4:

The idea is that you will have one list ('data') and each
item/element in that list is itself a list. Those sublists 
each correspond to one row from the data file.

Like this: 
list_of_lists = []
then after reading in the file:
list of lists = [[1, 2, 3], 
			  	 [4, 5, 6],  <- one row from file
			  	 [7, 8, 9]]
"""
import csv
from datetime import datetime
#import dateutil.parser as parser
import pandas as pd


# Create function to calculate daily trip duration, the 5 most popular starting and ending stations, the number
# 		of members and casual users
#   the function is receiving the data in the format: [duration, start_station, end_station, member_casual]
def print_details(data_list):
	total_duration = 0
	number_of_trips = len(data_list)
	number_of_casual_users = 0
	number_of_members = 0
	counter_dict_start = {}
	num_max_freq_start = 0
	name_max_freq_start = ''
	counter_dict_end = {}
	num_max_freq_end = 0
	name_max_freq_end = ''

	for trip in data_list:
		total_duration += int(trip[0])
		if trip[3] == 'member':
			number_of_members += 1
		elif trip[3] == 'casual':
				number_of_casual_users += 1
		else:
			continue

		if trip[1] in counter_dict_start:  # checking if the name is already in the dictionary
			counter_dict_start[trip[1]] += 1  # if yes, adding 1 to the counter
			if counter_dict_start[trip[1]] >= num_max_freq_start:  # checking if current frequency is the max
				num_max_freq_start = counter_dict_start[trip[1]]
				name_max_freq_start = trip[1]
		else:
			counter_dict_start[trip[1]] = 1

		if trip[2] in counter_dict_end:  # checking if the name is already in the dictionary
			#print ('been here!')
			counter_dict_end[trip[2]] += 1  # if yes, adding 1 to the counter
			if counter_dict_end[trip[2]] >= num_max_freq_end:  # checking if current frequency is the max
				#print('been here!')
				num_max_freq_end = counter_dict_end[trip[2]]
				name_max_freq_end = trip[2]
		else:
			counter_dict_end[trip[2]] = 1

	average_duration = round(total_duration / number_of_trips, 2)
	print('   The average daily duration is', average_duration, 'minutes')
	print('   The most popular starting station is', name_max_freq_start)
	print('   The most popular ending station is', name_max_freq_end)
	print('   The number of casual users is', number_of_casual_users)
	print('   The number of members is', number_of_members)

	return

fmt = '%Y-%m-%d %H:%M:%S'

# Open first csv and extract the list
infile_cvs1 = open('JC-201611-citibike-tripdata.csv', 'r')
data_first = []  # <- our empty list
csv_parsed1 = csv.reader(infile_cvs1)  # Compiling CSV file into lists

# Loop through the first file
#   the records are saved in the format: [duration, start_station, end_station, member_casual]
for row_csv1 in csv_parsed1:
	processing_list = []
	if row_csv1[12] == 'Subscriber' or row_csv1[12] == 'Customer':
		start_time = datetime.strptime(row_csv1[1], fmt)
		end_time = datetime.strptime(row_csv1[2], fmt)
		time_diff = round((end_time - start_time).total_seconds() / 60, 2)
		processing_list.extend([time_diff, row_csv1[4], row_csv1[8]])
	else:
		continue
	if row_csv1[12] == 'Subscriber':
		processing_list.append('member')
	if row_csv1[12] == 'Customer':
		processing_list.append('casual')
	data_first.append(processing_list)  # <- added this row to the lists of lists


# Open the second csv and extract the list
#   the records are saved in the format: [duration, start_station, end_station, member_casual]
infile_csv2 = open('JC-202111-citibike-tripdata.csv', 'r')
data_second = []  # <- our empty list
csv_parsed2 = csv.reader(infile_csv2)  # Compiling CSV file into lists

# Loop through second file
for row_csv2 in csv_parsed2:
	processing_list = []
	if row_csv2[12] == 'member' or row_csv2[12] == 'casual':
		start_time = datetime.strptime(row_csv2[2], fmt)
		end_time = datetime.strptime(row_csv2[3], fmt)
		time_diff = round((end_time - start_time).total_seconds() / 60, 2)
		processing_list.extend([time_diff, row_csv2[4], row_csv2[6], row_csv2[12]])
	else:
		continue
	data_second.append(processing_list)  # <- added this row to the lists of lists


# Call function for each file
print('\n-- Processing the first file...')
print_details(data_first)
print('\n-- Processing the second file...')
print_details(data_second)

# Close files
infile_cvs1.close()
infile_csv2.close()

# the following is the pandas portion
print('\n-- Working now with pandas...')

# creating a list with the header names
# header_names = ['date', 'trips24', 'cum_trips', 'miles_today', 'miles_todate',
#    'tot_annual_members', 'annual_members', '24h_passes', '7d_passes']

# reading their 2 files into a pandas structure and printing its lenght
txt_portion = pd.read_csv('JC-201611-citibike-tripdata.csv', sep=",", header=None)
# txt_portion.columns = header_names
print('\n   The number of rows in the pandas from the 1st file is:', len(txt_portion.axes[0]))

csv_portion = pd.read_csv('JC-202111-citibike-tripdata.csv', sep=",", header=None)
# csv_portion.columns = header_names
print('   The number of rows in the pandas from the 2nd the file is:', len(csv_portion.axes[0]))

# using the 'concat' functions to join/append the dataframes into one
merged_data = pd.concat([txt_portion, csv_portion], axis=0)

# printing the lenght of new dataframe
print('   The size of the the new/merged dataframe is:')
print('    number of rows:', len(merged_data.axes[0]))
print('    number of columns:', len(merged_data.axes[1]))

print('\n--- This is the end of the files processing ---')
