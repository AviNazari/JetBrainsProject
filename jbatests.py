scores = input().split()
total = len(scores)
corr = 0
incorr = 0
score_print = 0
if 15 <= total <= 50:
    for score in scores:
        if score == 'C':
            corr += 1
        if score == 'I':
            incorr += 1
            if incorr == 3:
                score_print = corr

    if incorr >= 3:
        print('Game over')
        print(score_print)
    elif incorr < 3:
        print('You won')
        print(score_print)
else:
    print('wrong number of inputs')
# put your python code here
