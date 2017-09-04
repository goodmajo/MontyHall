import secrets
from random import *

def main():
    exitFlag = False
    possibleChoices = [ 1, 2, 3 ]
    while exitFlag == False:
        carNumber = randint(1,3)
        startOverFlag = False
        while startOverFlag == False:
            userChoice = int(input('Please choose a number between 1 and 3. The right number gets a car: '))
            if userChoice != carNumber:
                print('I will now give you a peek behind one of the doors you did not choose:')
                goatDoor = set(possibleChoices).symmetric_difference([userChoice, carNumber])
                print('Baaaaa! There is a goat behind door number ', list(goatDoor)[0])
                userChoice2 = input('Would you like to change your choice? Type Yes or No: ')
                userChoice2 = userChoice2.lower()
                if userChoice2 == 'yes':
                    print('YOU WIN A CAR!!!!')
                    startOverFlag = True
                if userChoice2 == 'no':
                    print('Sorry, you chose the goat. You blew it!')
                    startOverFlag = True
            if userChoice == carNumber:
                print('I will now give you a peek behind one of the doors you did not choose:')
                goatDoorPossibilities = set(possibleChoices).symmetric_difference([carNumber])
                goatDoor = secrets.choice(list(goatDoorPossibilities))
                print('Baaaaa! There is a goat behind door number ', goatDoor)
                userChoice2 = input('Would you like to change your choice? Type Yes or No: ')
                userChoice2 = userChoice2.lower()
                if userChoice2 == 'no':
                    print('YOU WIN A CAR!!!!')
                    startOverFlag = True
                if userChoice2 == 'yes':
                    print('Sorry, you chose the goat. You blew it!')
                    startOverFlag = True

if __name__ == "__main__":
    main()