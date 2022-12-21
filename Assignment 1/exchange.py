#Author: Pankhuri
#Description: This program converts US dollar to INR

while True:
   USD= input("How many US Dollar do you want to exchange?-Type the value or done to exit:")
   if USD == 'done':
       print('\n Thanks for using this tool \n')
       break

 # checking if input is numeric or else start the loop
   if USD.isdigit() == False:
       print('\n Input a number, not letters \n')
       continue

   a= input('Enter the name of the currency you are converting to:')

   INR= input('What is the exchange rate?')
   if INR.isdigit() == False:                                            #checking if input is numeric
       print('\n Input a number')
       continue


   print('\n You can exchange', USD, 'us dollars for', int(USD)*int(INR), a, '\n')   #output statement
   print('Thanks for using this tool!')





