def minion_game(string):
    # your code goes here
    Kevin = 0
    Stuart = 0
    #lenstr = len(string)+1
    for item in range(len(string)):
        vowels = ['A', 'E', 'I', 'O', 'U']
        if string[item] in vowels:
            Kevin += len(string) - item
        else:
            Stuart += len(string) - item 
    if  (Kevin > Stuart): 
        print("Kevin", Kevin) 
    elif (Kevin < Stuart):
        print("Stuart", Stuart)
    else:
        print("Draw")

word = input()
minion_game(word)