from Choice import Choices


class Main:

    choices = Choices()

    print(''' 
    Welcome to the plant repository!
    
    What you want to do?
    
    Select 1 if you want to display a list of plants in the repository
    Select 2 if you want to learn more about the selected plant
    Select 3 if you want to add a new plant to the repository
    ''')

    choice = input('Your choice:')

    if choice == '1':
        choices.choice1()
    elif choice == '2':
        choices.choice2()
    elif choice == '3':
        choices.choice3()
    else:
        print("Hey! You can enter numbers from 1 to 3 ! Try again")
