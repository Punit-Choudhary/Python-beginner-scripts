x = input()
sum = 0
for i in x:
    z = int(i)
    sum += z**3
if sum == int(x):
    print('Armstrong')
else:
    print('Not Armstrong')
