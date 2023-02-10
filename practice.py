
# Password checker
# Create a variable here with the value of None
input_password = None
password_attempts = []
# While loop: if the password is not match
while input_password != '3x@mplePASS':
  # Ask to enter a password
  input_password = input("Enter your password: ")
  # if the entered password does not match
  if(input_password != '3x@mplePASS'):
    # print the "Password is incorrect. Please try again."
    print("Password is incorrect. Please try again.")
    password_attempts.append(input_password)
    
  print("" + str(password_attempts))

# Print if the password is successful.
print("Welcome!")



# for i in range(3):
#   for j in range(7, 12, 2):
#     print(j)

# for i in range(3):
#   for j in range(2):
#     print("hip", end=" ")
#   print("hooray!")
  
  
  
  
# num = 0
# while num < 10:
#   num = num + 1
#   print(num)
#   for i in range(3):
#     print("I belongs to " + str(num))
#     for j in range(1, 12, 3):
#       print("Do it more times " + str(i))
#   print("Next outer loop, please.")