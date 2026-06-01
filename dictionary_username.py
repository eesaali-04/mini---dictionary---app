login_dict = {}
while True:
    print('Welcome to the login app.\n')
    print('1) Add a username to the login dictionary. ')
    print('2) Find a password for a username. ')
    print('3) Show all the usernames. ')
    print('4) Delete a username from the dictionary. ')
    print('5) Exit. ')

    choice = input('Enter a choice between 1 to 5. ')

    if choice == '1':
        username = input('Enter the username: ').lower()
        password = input('Enter the password of the username: ').lower()
        login_dict[username] = password
        print(f'{username} added successfully to the login dictionary. ')

    elif choice == '2':
        username = input('Enter the username that you want to find out what the password is: ').lower()
        if username in login_dict:
            print(f'{username}: {login_dict[username]}')
        else:
            print(f'The username {username} is not in the dictionary. ')
