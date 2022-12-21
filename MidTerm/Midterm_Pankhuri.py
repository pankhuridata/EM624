#Author: Pankhuri

#Section 2:Code Checking

#Part 1:Corrected Code
N = input("Enter your characters: ")
L = ""
for letters in N:
    L=L+letters*3
print(L)

#Part 2:Corrected Code
handle = open('word_list-1.csv', 'r')
top2 = ["", ""]
for line in handle:
# For each line in the file, strip the input and put it into the word variable
    word = line.strip()
# Compare the length of each incoming word to the length of each word in each position
    for i in range(0,2):
        top2.sort(key=len)
        if len(word) > len(top2[i]):
            top2[i] = word
#Print the words
print("\nThe 2 longest words are:", top2)

#Part 3:Corrected Code
while True:
# prompts and receives user input
    char = input('\n Please enter an alphabetical character:')
    if char == 'done':
        print('\n')
        break
    else:
        if char.isdigit():      #checks if input is more than one character
            print('Invalid input.')
        else:
            if len(char) > 1:
                print('Invalid input.')
            else:
                if char in "aeiou":
                    print('False')
                else:
                    print('True')


#Section 3: Writing Code

# Part 4:

from collections import Counter

with open('ai_trends.txt', 'r') as f:              #read file and make list
    data = f.read()
    data_into_list = data.split()


with open('stopwords_en.txt', 'r') as f:               #read another file and make another list
    data_1 = f.read()
    data_eliminate = data_1.split()

data_into_list.sort()                                    #sort the list
data_eliminate.sort()
new_list = []
for word in data_into_list:                                  #for each word in line.split()
    if word not in data_eliminate:                            #if a word isn't in line.split
        new_list.append(word)

Counter = Counter(new_list)                       #Counting occurance of each word and making a dict

most_occur = Counter.most_common(5)                             #5 most common occurance
print('Five most common occurance are', most_occur)

least_common = Counter.most_common()[:-5-1:-1]                         #5 least common occurance
print('Five least common occurance are,', least_common)

avr = sum(Counter.values())/len(Counter.values())             #Averaging the occurance of each word by total number of occurance of all words
print('The Average occurance of the words is', round(avr, 1))


new_list.sort(key=len)                                            #longest and shortest words
print("The longest word in the list is '",new_list[-1],"'")
print("The shortest word in the list is '",new_list[0],"'")

test_list = list(set(new_list))                                 #list for uniques words

avg = sum(map(len, test_list))/float(len(test_list))            #averaging word length for unique words

print("The Average length of unique words in the list rounded to nearest integer is : ", round(avg))

#Part 5:

import pandas as pd
from collections import Counter
import csv
file_csv = pd.read_csv('cars.csv', index_col=False)


print("First Three rows of the data frame:")             #prints the first 3 rows
print(file_csv.head(3))
print("Last three rows of the data frame:")               #prints the last 3 rows
print(file_csv.tail(3))



with open('cars.csv', newline='') as f:
    reader = csv.reader(f)
    your_list = list(reader)

ratio = []
for i in range(1,len(your_list)):
    ratio.append(float(your_list[i][8])/float(your_list[i][7]))


ratio.sort()

ratio[0:5]

print('\n This is the end of the files processing')