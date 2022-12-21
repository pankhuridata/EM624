#Author:Pankhuri
#Description: Part1

n0=0                                                             #initializing the variable as instructed
n1=0
n2=0
with open("NYC-CitiBike-Jan_Feb2016.csv") as in_file:                  #opening a file
 citi=in_file.readlines()                                              #reading the lines
 n0 = sum(1 for line in citi)                                          #count total number of lines

 print("These are the last five lines in the file")                                #printing the last five lines
 last_lines = citi[-5:]
 print(last_lines)

 for a in citi:
    a=a.strip().split(",")                                  #strip() removes all whitespaces split(",") because its csv

    if a[13] =="Customer":                                 #count of the number of lines with "Customer" as usertype
        n1+=1
    elif a[13] =="Subscriber":                             #count of the number of lines with "Subscriber" as usertype
        n2+=1

z1=(n1/n0)*100

print('\n')
print("The file has", n0, "lines. Of those", n1,"have usertype as Customer,", n2," have usertype as Subscriber. Customer are ", z1, "of total lines")

# Author: Pankhuri
#Description: Part 2

n3=0
n4=0
n5=0
with open("NYC-CitiBike-Apr_May2016.csv") as in_file:
 bike=in_file.readlines()
 n3 = sum(1 for line in bike)                                           #count of the number of lines

 print('\n')
 print("These are the First five lines in the file")                                #printing the first five lines
 first_lines = bike[1:6]
 print(first_lines)

 for a in bike:
    a=a.strip().split(",")                                  #strip() removes all whitespaces split(",") because its csv

    if a[13] =="Customer":                                 #count of the number of lines with "Customer" as usertype
        n4+=1
    elif a[13] =="Subscriber":                             #count of the number of lines with "Subscriber" as usertype
        n5+=1

z2=(n4/n3)*100

print('\n')
print("The file has", n3, "lines. Of those", n4,"have usertype as Customer,", n5," have usertype as Subscriber. Customer are", z2, "% of the total.")
print('\n')


#Author: Pankhuri
#Description: Part 3
if n0>n3:
    print("The Winter riders are more than the Spring")
else:
    print("The Spring riders are more than the Winter")

if z1>z2:
    print("During the Winter there are more Customers/non-Subscribers than in the Spring")
else:
    print("During the Spring there are more Customers/non-Subscribers than in the Winter")

