# this code will genrate pattern number #13
size = 5
for i in range(size):
    print(" ".join([str(x+1) for x in range(i+1)]) + ' *'*(size-i-1))
