filename = 'Guest.txt'
userin = 'placeholder'

print('type start')

while userin != 'quit':
    if userin == 'Start':
        User = input('Hello, User. What is your name? ' + '\n')
        with open(filename, 'a') as file_object:
            file_object.write('users name is ' + User + '\n')
        print('welcome ' + User)
