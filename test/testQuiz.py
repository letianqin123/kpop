'''Letian Qin
   April 22, 2023
   Spring 2023, CS 5001
   This file tests the Quiz class
'''

from Quiz import Quiz
from Songplayer import Songplayer
from datetime import datetime

def test_init(quiz, expected_level, expected_points):
    '''this function tests the attributes of a songplayer'''

    # compare the level of a quiz with the expected value
    if quiz.level == expected_level:
        print("passed")
    else:
        print("failed")

    # compare the points of a quiz with the expected value
    if quiz.points == expected_points:
        print("passed")
    else:
        print("failed")


def test_get_certificate(quiz, level, name, expected):
    '''this function tests the get_certificate method of a songplayer'''

    # print out the expected value
    print("expected:")
    print(expected)
    
    # print out the actual value
    print("gives:")
    quiz.get_certificate(level, name)


def test_play(quiz, level, name, expected):
    '''this function tests the play method of a songplayer'''

    # print out the expected value
    print("expected:")
    print(expected)
    
    # print out the actual value
    print("gives:")
    quiz.play(level, name)


def main():
    
    # testing with correct data1
    test1 = Quiz("1") 
    test_init(test1, "1", 2) 
    test_get_certificate(test1, "1", "bill", "certificate-like output with the name 'bill', current time and difficulty level: easy") 
    test_play(test1, "1", "bill", "three easy songs quiz with infinite playback chances, generates certificate when winning")


    # testing with correct data2
    test2 = Quiz("3") 
    test_init(test2, "3", 0) 
    test_get_certificate(test2, "3", "jolin", "certificate-like output with the name 'jolin', current time and difficulty level: hard")
    test_play(test2, "3", "jolin", "seven hard songs quiz with no playback chance, generates certificate when winning")
    
    # testing with incorrect data
    print("expected:")
    print("ValueError: level must be '1' or '2' or '3'")  
    print("gives:")
    Quiz(100) 


if __name__ == "__main__":
    main() 
