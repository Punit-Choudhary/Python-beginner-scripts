# this code will give us the required pattern number 16

for i in range(5):
    print('* '*(5-i-1) + "{} ".format(i+1)*(i+1))
