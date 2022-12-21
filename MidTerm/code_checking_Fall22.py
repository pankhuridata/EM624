#----1----
# --Original code
N = input("Enter your characters: ")
L = []
for letters in N:
    letters.split()
    L.append(letters)
    print (L*3)


#----2----
# --Original code
handle = open('word_list.csv','r')
top2 = ["",""]
for line in handle:
   #For each line in the file, strip the input and put it into the word variable
   word = line.strip()
   #Compare the length of each incoming word to the length of each word in each position
   for i in range(0,2):
      top2.sort(key = len)
      if (len(word) < len(top2[i])):
         top2[i] = word
#Print the words
print ("\nThe 2 longest words are:"), top2


#----3----
# --Original code
while True:
    #prompts and receives user input
    char = input('Please enter an alphabetical character:')
    if len(char) > 1: #checks if input is more than one character
        print ('Invalid input')
    else:
        if char == 'a' or 'e' or 'i' or 'o' or 'u' or 'y': #checks if input is a vowel
            print ('False')
    else:
        print ('True')
