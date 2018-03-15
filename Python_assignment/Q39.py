'''
Write a program able to play the "Guess the number"-game, where the number to be guessed is randomly chosen between 1 and 20. (Source: http://inventwithpython.com) This is how it should work when run in a terminal.
'>>> import guess_number
Hello! What is your name?
Torbjörn
Well, Torbjörn, I am thinking of a number between 1 and 20.
Take a guess.
10
Your guess is too low.
Take a guess.
15
Your guess is too low.
Take a guess.
18
Good job, Torbjörn! You guessed my number in 3 guesses!
'''



import random
def guess_the_no():
    print ("Hello! What is your name?")
    name = str(input())
    print ("Well, "+name+', I am thinking of a number between 1 and 20.')
    print ('Take a guess.')
    m = int(input())
    n = random.choice(range(1,20))
    cnt=1
    while m!=n:
        cnt+=1
        if m>n:
            print ("Your guess is too high")
        else:
            print ("Your guess is too low")
        print ("Take a guess.")
        m = int(input())
    print ("Good job, "+name+"! You guessed my number in "+str(cnt)+" guesses!")

guess_the_no()
