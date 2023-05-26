#import random module
import random

#define variables
timmy_home = False
score = 0

#define functions
def find_home():
    global timmy_home
    global score
    timmy_home = True
    score += 10
    print("You found your way home! You win!")

def get_lost():
    global timmy_home
    global score
    timmy_home = False
    score -= 5
    print("You got lost! You have to start over.")

#main game loop
while not timmy_home:
    #generate random number
    rand_num = random.randint(1, 10)
    #check if random number is 1 or 2
    if rand_num == 1:
        find_home()
    elif rand_num == 2:
        get_lost()
    else:
        #generate random number for positive or negative outcome
        rand_num_2 = random.randint(1, 2)
        if rand_num_2 == 1:
            score += 1
            print("You made a good choice! Your score is now:", score)
        else:
            score -= 1
            print("You made a bad choice! Your score is now:", score)
