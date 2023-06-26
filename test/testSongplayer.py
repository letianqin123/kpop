'''Letian Qin
   April 22, 2023
   Spring 2023, CS 5001
   This file tests the Songplayer class
'''

from Songplayer import Songplayer
from playsound import playsound

def test_init(songplayer, expected_level, expected_songs):
    '''this function tests the attributes of a songplayer'''

    # print out the expected level
    print("expected level:")
    print(expected_level)
    
    # print out the actual level
    print("gives:")
    print(songplayer.level)

    print("*" * 30)

    # print out the expected songs
    print("expected songs:")
    print(expected_songs)
    
    # print out the actual level
    print("gives:")
    print(songplayer.songs)

    print("*" * 30)


def test_play(songplayer, path, expected):
    '''this function tests the play method of a songplayer'''
    
    # print out the expected song being played
    print("expected:")
    print("plays " + expected)
    
    # use the play method to play the song
    print("gives:")  
    songplayer.play(path)


def main():
    
    # testing with correct data1   
    test1 = Songplayer("2")   
    test_init(test1, "2", {"cupid" : "medium short/Cupid - FIFTY FIFTY.mp3",
                        "ditto" : "medium short/Ditto - NewJeans.mp3",
                        "flower" : "medium short/FLOWER - JISOO.mp3",
                        "la di da" : "medium short/LA DI DA - EVERGLOW.mp3",
                        "zero" : "medium short/Zero - NewJeans.mp3"})
    test_play(test1, "medium short/Ditto - NewJeans.mp3", "ditto")

    # testing with correct data2   
    test2 = Songplayer("1")  
    test_init(test2, "1", {"shut down" : "easy short/Shut Down - BLACKPINK.mp3",
                        "love dive" : "easy short/LOVE DIVE - IVE.mp3",
                        "antifragile" : "easy short/ANTIFRAGILE - LE SSERAFIM.mp3"})
    test_play(test2, "easy short/ANTIFRAGILE - LE SSERAFIM.mp3", "antifragile")

    # testing with incorrect data
    print("expected:")
    print("ValueError: level must be '1' or '2' or '3'")  
    print("gives:")
    Songplayer(0)
    

if __name__ == "__main__":
    main() 
