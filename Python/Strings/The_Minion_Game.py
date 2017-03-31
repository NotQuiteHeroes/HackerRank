'''
Kevin and Stuart want to play the 'The Minion Game'.
Game Rules
Both players are given the same string, s.
Both players have to make substrings using the letters of the string s.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels. 
The game ends when both players have made all possible substrings. 
Scoring
A player gets +1 point for each occurrence of the substring in the string s.
For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points. 
Your task is to determine the winner of the game and their score.
Input Format
A single line of input containing the string s. 
Note: The string  will contain only uppercase letters: A-Z.
Output Format
Print one line: the name of the winner and their score separated by a space.
If the game is a draw, print Draw.
https://www.hackerrank.com/challenges/the-minion-game
'''

if __name__ == '__main__':
    s = raw_input()
    minion_game(s)
    
def minion_game(string):
    vowels = ['A', "E", "I", "O", "U"]
    stuartScore = 0
    kevinScore = 0
    for i in xrange(len(string)):
        if string[i] in vowels:
            kevinScore+= len(string) - i
        else:
            stuartScore+= len(string) - i
    if(stuartScore > kevinScore):
        print("Stuart %d" % stuartScore)
    elif(kevinScore > stuartScore):
        print("Kevin %d" % kevinScore)
    else:
        print("Draw")
