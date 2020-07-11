import math
starting_atoms = int(input())
resulting_atoms = int(input())
division = round(starting_atoms / resulting_atoms)
print(division)
x = round(math.log(division, 2))

print(x)




nums = []
sum = 0
input()
for i in range(int(input())):
    print(i)
    if str(input()) == '.':
        break
    else:
        nums.append(i)
mean = sum(nums) / len(nums)
print(mean)
