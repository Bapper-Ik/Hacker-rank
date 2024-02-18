
'''
Task
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules
Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string S.
Your task is to determine the winner of the game and their score.


'''

def minion_game(string):
    kevin_score = 0
    staut_score = 0
    length = len(string)
    vowels = "AEIOU"

    for i in range(len(string)):
        if string[i] in vowels:
            kevin_score += length - i
        else:
            staut_score += length - i

    if kevin_score > staut_score:
        print("Kevin", kevin_score)
    elif kevin_score < staut_score:
        print("staut", staut_score)
    elif kevin_score == staut_score:
        print("Draw")


s = "BANANA"
minion_game(s)

