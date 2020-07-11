import random


def get_score(u_name):
    file = open('rating.txt', 'r')
    initial_score = 0
    for line in file:
        if u_name in line:
            user_data = list()
            user_data.append(line)
            for item in user_data:
                current_score = int((item.split()[1]))
                initial_score += current_score
    file.close()
    return initial_score


def win_lose(u_input, all_options):

    op_index = all_options.index(u_input)
    new_list = all_options[op_index + 1:] + all_options[0:op_index]
    winners = []
    losers = []
    half = len(new_list) // 2
    for i in range(0, len(new_list)):
        if i < half:
            winners.append(new_list[i])
        elif half <= i < len(new_list):
            losers.append(new_list[i])

    return winners, losers


def play_game(all_ops=None):
    try:
        global user_score
        user_input = input()
        if user_input == '!exit':
            print('Bye!')
            exit()

        elif user_input == '!rating':
            print(user_score)

        elif user_input in all_ops:
            winners, losers = win_lose(user_input, all_ops)
            rand_option = random.choice(all_ops)
            if rand_option in winners:
                print(f"Sorry, but computer chose {rand_option}")
            elif rand_option in losers:
                print(f"Well done. Computer chose {rand_option} and failed")
                user_score += 100
            elif rand_option == user_input:
                print(f"There is a draw ({user_input})")
                user_score += 50

        elif user_input in ['rock', 'scissors', 'paper']:

            all_ops = ['rock', 'scissors', 'paper']
            wins = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
            rand_option = random.choice(all_ops)
            if user_input == wins[rand_option]:
                print(f"Sorry, but computer chose {rand_option}")
            elif user_input == rand_option:
                print(f"There is a draw ({user_input})")
                user_score += 50
            else:
                print(f"Well done. Computer chose {rand_option} and failed")
                user_score += 100

        else:
            print('Invalid input')
    except Exception as e:
        print(e)


username = input('Enter your name: ')
print('Hello, ' + username)

given_options = input()
list_of_options = given_options.split(', ')
print("Okay, let's start")

if given_options is None:
    list_of_options = ['rock', 'scissors', 'paper']

user_score = get_score(username)

while True:
    play_game(list_of_options)