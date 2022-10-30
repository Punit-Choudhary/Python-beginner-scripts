x = input()
sum = 0
for i in x:
    z = int(i)
    sum += z**len(x)
if sum == int(x):
    print('Armstrong Number')
else:
    print('Not an Armstrong Number')
