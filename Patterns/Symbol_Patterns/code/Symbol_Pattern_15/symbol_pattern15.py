# size is decided by n
# this piece of code is written to specially make the pattern of img file 15
n = 5
for i in range(n):
    print(" ".join([str(x+1) for x in range(n-i)]) + ' *'*(i+1))
