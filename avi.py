taxable_income = int(input())

if 0 <= taxable_income <= 15527:
    rate = 0
    tax = round((taxable_income * rate)/100)
elif 15528 <= taxable_income <= 42707:
    rate = 15
    tax = round((taxable_income * rate)/100)
elif 42708 <= taxable_income <= 132406:
    rate = 25
    tax = round((taxable_income * rate)/100)
else:
    rate = 28
    tax = round((taxable_income * rate)/100)

output = 'The tax for {income} is {percent}%. That is {calculated_tax} dollars!'.format(income=taxable_income,
                                                                                        percent=rate,
                                                                                        calculated_tax=tax)
print(output)




def heading(word, level=1):
    word = str(word)
    if level < 1:
        level = 1
    elif level > 6:
        level = 6
    return str((int('#') ** level) + (word))
