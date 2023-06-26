'''Letian Qin
   April 22, 2023
   Spring 2023, CS 5001
   This file implements the main function of the project
'''

from Quiz import Quiz


def main():
    '''This is the main control function for the program.'''

    print("welcome to the Guess the K-Pop Song game!")
    
    # use the try except syntax to handle potential errors
    try: 

        # ask for player's name
        name = input("please enter your name")

        # ask for the difficulty level the player wants
        difficulty = input("enter 1 for easy level \n2 for medium level \n3 for hard level")

        # if the difficulty level is not 1 or 2 or 3, use a while loop to repeatedly ask for new input
        while difficulty != "1" and difficulty != "2" and difficulty != "3":
            print("must enter 1 or 2 or 3")
            difficulty = input("enter 1 for easy level \n2 for medium level \n3 for hard level")

        # create a quiz based on the difficulty level the player chose
        quiz = Quiz(difficulty)

        # play the quiz by calling the play method
        quiz.play(difficulty, name)
    
    # print out information about the error if any occurs
    except TypeError as ex:
        print("invalid type:", ex)
    
    except ValueError as ex:
        print("invalid value:", ex)

    except FileNotFoundError as ex:
        print("audio files can't be found:", ex)


if __name__ == "__main__":
    main()