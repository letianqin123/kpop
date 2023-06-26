'''Letian Qin
   April 22, 2023
   Spring 2023, CS 5001
   This file implememts the Quiz class
'''

from Songplayer import Songplayer
from datetime import datetime

class Quiz:
    ''' Class: Quiz
        Attributes: level, points
        Methods: get_certificate, play'''
    
    def __init__(self, level):
        ''' Constructor
            Parameters:
                self
                level - the difficulty level the player chooses'''
        
        self.level = level

        # the quiz has different starting points based on different difficulty levels
        # easy level has 2 starting points
        if level == "1":
            self.points = 2

        # medium level has 1 starting points            
        elif level == "2":
            self.points = 1
        
        # hard level has no starting points
        elif level == "3":
            self.points = 0

        # raise a value error if level is not 1 or 2 or 3
        else:
            raise ValueError("level must be '1' or '2' or '3'") 


    def get_certificate(self, level, name):
        ''' the get_certificate method generates congratulatory information for the player
            Parameters:
                self
                name - name of the player
                level - difficulty level
            Return:
                nothing'''
        
        # use the datetime class of the datetime module to get current date and time
        now = datetime.now()
        time = now.strftime("%d/%m/%Y %H:%M:%S")
        
        # translate the difficulty level to be used in the certificate
        if level == "1":
            difficulty = "easy"
        elif level == "2":
            difficulty = "medium"
        elif level == "3":
            difficulty = "hard"
        # raise a value error if level is not 1 or 2 or 3
        else:
            raise ValueError("level must be '1' or '2' or '3'") 

        # print the certificate
        print("*" * 80)
        print("\n")
        print("Congrats! You won!".center(80)) # use the center() method to center the messages
        second_line = "This is to certify that on " + time + ","
        print(second_line.center(80))
        third_line = name + " conquered the Guess the K-Pop Song game at difficulty level: " + difficulty
        print(third_line.center(80))
        print("\n")
        print("*" * 80)


    def play(self, level, name): 
        ''' the play method starts the game
            Parameters:
                self
                name - name of the player
                level - difficulty level
            Return:
                congratulatory information or game over information'''
        
        # create a songplayer based on the difficulty level the player chose
        player = Songplayer(level)
  
        # countdown to the first song being played        
        print("starting 3...")
        print("2...")
        print("1!")  
        print("*" * 30)
        print("first song playing...")

        # use a for loop to go through all the songs in the songplayer        
        for item in player.songs:

            # use the play method of the songplayer class to play each song
            player.play(player.songs[item])

            # for easy level, the player can listen to the song repeatedly
            # use a while loop to repeatedly ask if the player wants to listen again
            if level == "1":
                answer = input("want to hear it again? y/n")

                # if the answer is neither y or n, use a while loop to repeatedly ask for new input
                while answer.lower()[0] != "y" and answer.lower()[0] != "n":
                    print("must enter y or n")
                    answer = input("want to hear it again? y/n")
                
                # if the answer is y, use the play method of the songplayer class to play the song and ask again
                while answer.lower()[0] == "y":
                    player.play(player.songs[item])
                    answer = input("want to hear it again? y/n")

                    # if the answer is neither y or n, use a while loop to repeatedly ask for new input
                    while answer.lower()[0] != "y" and answer.lower()[0] != "n":
                        print("must enter y or n")
                        answer = input("want to hear it again? y/n")
            
            # for medium level, the player can listen to the song once again
            # use a conditional to ask if the player wants to listen again
            elif level == "2":
                answer = input("want to hear it again? y/n")

                # if the answer is neither y or n, use a while loop to repeatedly ask for new input
                while answer.lower()[0] != "y" and answer.lower()[0] != "n":
                    print("must enter y or n")
                    answer = input("want to hear it again? y/n")

                # if the answer is y, play the song once
                if answer.lower()[0] == "y":
                    player.play(player.songs[item])
            
            # raise a value error if level is not 1 or 2 or 3
            elif level != "1" and level != "2" and level != "3":
                raise ValueError("level must be 1 or 2 or 3") 

            # check the player's guess 
            # if guessed wrong, add 1 point, otherwise subtract 1 point
            guess =  input("what's the song?")
            if guess.lower() == item:
                self.points += 1
                print("you got it right!" + "\n""you have " + str(self.points) + " points left")
            else:
                self.points -= 1
                print("yikes! wrong answer. the song is " + item + "\n""you have " + str(self.points) + " points left")
            
            # check the points
            if self.points > 0:  

            # if points are bigger than 0 and the current song is not the last song 
                if item != list(player.songs.items())[-1][0]:

                    # ask if the player is ready to listen to the next song
                    answer = input("press any key to listen to the next song")
                    print("*" * 30)
                    print("next song playing...")

            # if the points are equal to or less than 0, end the game
            else:
                print("*" * 30)
                print("\n")
                print("GAME OVER!!!".center(30))
                print("\n")
                print("*" * 30)
                return

        # after the game, call the get_certificate to print out a certificate for the player
        return self.get_certificate(level, name)
            






