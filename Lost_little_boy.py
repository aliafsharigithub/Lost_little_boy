import random
#these are bad choices
trap = "You fell in to a Trap"
fire = "You’ve caught on Fire"
monkeys = "You’ve got beat up by monkeys"
#this is the deadly choice
drown = "You’ve drowned"
#these are right choices
bridge = "You found the bridge"
river = "You found the river"
route = "You found a route"
boat = "You found a boat"
lighthouse = "You found the lighthouse"
#this is the winning choice
home = "you found home"
right_choices = [bridge, river, route, boat, lighthouse]
wrong_choices = [trap, fire, monkeys]
wrong = random.choice(wrong_choices)
right = random.choice(right_choices)
choices = [right, wrong, home,drown]
print ("where am I?")
a = input()
print("I am totally lost")
a = input()
print("I have to find the way back home")
step = 10
while step >= 0:
    timmy = input("which way should I go? Right or left: ")
    step = step - 1
    if timmy == "right":
        choice = random.choice(choices)
        print(choice)
        choices.remove(choice)
    elif timmy == "left":
        choice = random.choice(choices)
        print(choice)
        choices.remove(choice)
    elif choice == drown :
        print("you died")
        break
    elif choice == home :
        print("you survived")
        break
print("game over")
a = input()
