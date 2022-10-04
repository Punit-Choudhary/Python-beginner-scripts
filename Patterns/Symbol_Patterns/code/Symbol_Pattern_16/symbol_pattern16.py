# this code will give us the required pattern number 16
# img link: https://github.com/Punit-Choudhary/Python-beginner-scripts/blob/main/Patterns/Symbol_Patterns/img/16.PNG

for i in range(5):
    print('* '*(5-i-1) + "{} ".format(i+1)*(i+1))
