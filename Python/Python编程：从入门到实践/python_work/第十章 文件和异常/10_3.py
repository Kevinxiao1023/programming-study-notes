name = input("Please type your name here:")
filename = 'guest.txt'
with open (filename, 'w') as file_object:
    file_object.write(name.title())
