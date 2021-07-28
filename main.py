# password validatator
# first iam gonna make some variables for all the conditions on password validation,
# upper, lower, length(7-10), digit, symbol(@)
# setting it false in first
upper = False
lower = False
length = False
digit = False
symbol = "@"     # the symbol
symbol_pass = False  # symbol checker
# now getting the input from the user 
password_try = input("Enter your password here : ")
# now. using if and elif, iam checking the password is followed the conditions or not
# length 7 - 10 
if len(password_try) >= 7 and len(password_try) <= 10:
    length = True
    # making a for loop
    for letter in password_try:
      # lower check
      if letter.islower():
        lower = True
      # upper check
      elif letter.isupper():
        upper = True
      # digit check
      elif letter.isdigit():
        digit = True
      # symbol check
      elif symbol in password_try:
        symbol_pass = True

# now lets check the password is validit or not      
# if its all True, then its a valid password  
if upper and lower and length and digit and symbol_pass == True:
    print("This is a valid password")
# else not 
else:
  print("This password is not valid")

# end
