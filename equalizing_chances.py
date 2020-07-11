import random

user_input = input()
list_inputs = ['rock', 'scissors', 'paper']
rand_option = random.choice(list_inputs)
print(rand_option)

if user_input == 'rock':

    if rand_option == 'rock':
        print('There is a draw (rock)')
    elif rand_option == 'scissors':
        print('Well done. Computer chose scissors and failed')
    elif rand_option == 'paper':
        print('Sorry, but computer chose paper')

elif user_input == 'paper':

    if rand_option == 'rock':
        print('Well done. Computer chose rock and failed')
    elif rand_option == 'scissors':
        print('Sorry, but computer chose scissors')
    elif rand_option == 'paper':
        print('There is a draw (paper)')

elif user_input == 'scissors':

    if rand_option == 'rock':
        print('Sorry, but computer chose rock')
    elif rand_option == 'scissors':
        print('There is a draw (scissors)')
    elif rand_option == 'paper':
        print('Well done. Computer chose scissors and failed')

else:
    print('Invalid user input!')