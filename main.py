import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
options = [rock,paper,scissors]
valid = False
random_choice =random.randint(0,2)
option = int(input( " what do you choose type 0 for rock 1 for paper 2 for scissors "))
if option == 0:
    print(rock)
    if (options[random_choice]== scissors):
        valid = True
    elif (options[random_choice]== paper):
        valid = False
elif option == 1:
    print(paper)
    if (options[random_choice]== rock):
        valid = True
    elif (options[random_choice]== scissors):
        valid = False
elif option == 2:
    print(scissors)
    if (options[random_choice]== paper):
        valid = True
    elif (options[random_choice]== rock):
        valid = False
else:
    print("invalid option " + str(option))
print("computer choose" )
print(options[random_choice])

if(random_choice == option):
    print("a draw")
elif(valid == True):
    print("you win")
elif(valid == False):
    print("you lose")