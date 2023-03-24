#Password Username
Username = input("What is your name? ")
Password = input("What is your password? ")

x= len(Password)

print(f'Hello {Username}! Your password is {"*"*x} and {x} letters long')