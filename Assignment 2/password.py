#Author:Pankhuri
#Description: Validate the password according to the description: a)Minimum value=5 b)Maximum Value:12
#c)Any combination of numerical and alphabetical characters

sp="!@#$%^&*()-+?_=,<>/"
while True:
   p= input("Enter a password or done if you are finished:")   #input statement
   if p == 'done':
       print('\n Thanks for using this tool \n')
       break
#checking the length of the password
   if len(p)<5 or len(p)>12:
        print('Length of password should be between 5 to 12')
        continue
 #checking for only alphabetical and numberic values in password
   if any(c in sp for c in p):
      print('Can only contain numeric and alphabetical values')
      continue
   else:
    print('Password Accepted! GoodBye!')

