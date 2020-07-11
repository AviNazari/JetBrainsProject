import random
list_inputs = ['rock', 'scissors', 'paper']
wins = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
while True:
    try:
        user_input = input()
        if user_input == '!exit':
            print('Bye!')
            exit()
        if user_input in ('rock', 'paper', 'scissors'):
            rand_option = random.choice(list_inputs)
            if user_input == wins[rand_option]:
                print(f"Sorry, but computer chose {rand_option}")
            elif user_input == rand_option:
                print(f"There is a draw ({user_input})")
            else:
                print(f"Well done. Computer chose {rand_option} and failed")
        else:
            print('Invalid input')
    except Exception as e:
        print(e)