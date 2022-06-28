print('\n====== Welcome to Foyez Academic Library ======')

while(True):
    welcome_message = '''
Please choose an option:
Press 1 -For List all the books
Press 2 -For Request a book
Press 3 -For Return a book
Press 4 -For Exit the Library'''

    print(welcome_message)
    choose_option = int(input('\nChoose any Option: '))

    if choose_option == 1:
        print('Those Books are available: \n1 -Python \n2 -Django \n3 -MySQL')

    elif choose_option == 2:
        borrow_book = input('Enter Borrow Book Name: ')
        borrow_book = borrow_book.lower()

        if borrow_book == '1' or borrow_book == 'python':
            print(f'You have been issued Python Book. Please keep it safe and return it within 30 days')
        elif borrow_book == '2' or borrow_book == 'django':
            print(f'You have been issued Django Book. Please keep it safe and return it within 30 days')
        elif borrow_book == '3' or borrow_book == 'mysql':
            print(f'You have been issued MySQL Book. Please keep it safe and return it within 30 days')
        else:
            print('Sorry, This book is either not available or Invalid Oparetion.')

    elif choose_option == 3:
        return_book = input('Enter Return Book Name: ')
        return_book = return_book.lower()

        if return_book == 'python':
            print(f'Thanks for returning this Python Book! Hope you enjoyed reading it!')
        elif return_book == 'django':
            print(f'Thanks for returning this Django Book! Hope you enjoyed reading it!')
        elif return_book == 'mysql':
            print(f'Thanks for returning this MySQL Book! Hope you enjoyed reading it!')
        else:
            print('Sorry, You Enter Wrong Books Name.')

    elif choose_option == 4:
        print('Thanks for choosing Foyez Academic Library. Have a great day ahead!')
        break
    else:
        print('Please, Enter Valid Command.')