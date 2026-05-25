my_dict = {}
while True:
    print('Welcome to the mini dictionary app.\n')
    print('1) Add a word to the dictionary. ')
    print('2) Retrieve the meaning of a word. ')
    print('3) Show all the words. ')
    print('4) Delete a word from the dictionary. ')
    print('5) Exit. ')

    choice = input('Enter a choice between 1 to 5. ')
    if choice == '1':
        word = input('Enter the word: ').lower()
        meaning = input('Enter the meaning of the word: ').lower()
        my_dict[word] = meaning
        print(f'{word} added successfully to the dictionary')

    elif choice == '2':
        word = input('Enter the word that you want to find out the meaning: ').lower()
        if word in my_dict:
            print(f'{word}: {my_dict[word]}')
        else:
            print(f'The word {word} is not in the dictionary. ')
