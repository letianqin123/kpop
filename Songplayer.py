'''Letian Qin
   April 22, 2023
   Spring 2023, CS 5001
   This file implememts the Songplayer class
'''

from playsound import playsound

class Songplayer:
    ''' Class: Songplayer
        Attributes: level, songs
        Methods: play'''
    
    def __init__(self, level):
        ''' Constructor
            Parameters:
                self
                level - the difficulty level the player chose'''
        
        self.level = level

        # based on the difficulty level the player chose, the songplayer will have different set of songs
        # the song titles and paths to the song files are stored as pairs in different dictionaries
        # for easy level, the dictionary consists of three popular K-Pop songs
        if level == "1":
            self.songs = {"shut down" : "easy short/Shut Down - BLACKPINK.mp3",
                        "love dive" : "easy short/LOVE DIVE - IVE.mp3",
                        "antifragile" : "easy short/ANTIFRAGILE - LE SSERAFIM.mp3"}          
            
        # for medium level, the dictionary consists of five moderately popular K-Pop songs
        elif level == "2":
            self.songs = {"cupid" : "medium short/Cupid - FIFTY FIFTY.mp3",
                        "ditto" : "medium short/Ditto - NewJeans.mp3",
                        "flower" : "medium short/FLOWER - JISOO.mp3",
                        "la di da" : "medium short/LA DI DA - EVERGLOW.mp3",
                        "zero" : "medium short/Zero - NewJeans.mp3"}    

        # for hard level, the dictionary consists of seven K-Pop songs, some of which are b-sides or from less popular groups        
        elif level == "3":
            self.songs = {"2 baddies" : "hard short/2 Baddies - NCT 127.mp3",
                        "beautiful monster" : "hard short/BEAUTIFUL MONSTER - STAYC.mp3",
                        "blue" : "hard short/Blue - BIGBANG.mp3",
                        "bop bop" : "hard short/BOP BOP! - VIVIZ.mp3",
                        "left right" : "hard short/LEFT RIGHT - XG.mp3",
                        "mvsk" : "hard short/MVSK - Kep1er.mp3",
                        "no problem" : "hard short/NO PROBLEM (Feat. Felix of Stray Kids) - NAYEON.mp3"}
        
        # raise a value error if level is not 1 or 2 or 3
        else:
            raise ValueError("level must be '1' or '2' or '3'") 


    def play(self, path):
        ''' the play method plays the audio file of given path
            Parameters:
                self
                path - path to the audio file
            Return:
                nothing'''
        
        # call the playsound function from playsound module to play the audio file
        playsound(path)



