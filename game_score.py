import random

initial_score = 0
list_inputs = ['rock', 'scissors', 'paper']
wins = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}

username = input('Enter your name: ')
print('Hello, ' + username)

file = open('rating.txt', 'r')
for line in file:
    if username in line:
        user_data = list()
        user_data.append(line)
        for item in user_data:
            current_score = int((item.split()[1]))
            initial_score += current_score
            print(initial_score)
while True:
    try:
        user_input = input()
        if user_input == '!exit':
            print('Bye!')
            exit()
        elif user_input == '!rating':
            print(initial_score)
        elif user_input in ('rock', 'paper', 'scissors'):
            rand_option = random.choice(list_inputs)
            if user_input == wins[rand_option]:
                print(f"Sorry, but computer chose {rand_option}")
            elif user_input == rand_option:
                print(f"There is a draw ({user_input})")
                initial_score += 50
            else:
                print(f"Well done. Computer chose {rand_option} and failed")
                initial_score += 100
        else:
            print('Invalid input')
    except Exception as e:
        print(e)