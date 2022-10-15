# function to implement HCF
# hcf_ stores the hcf calculated
# k stores the minimum of two inputs
def HCF(n1, n2):
    k = 0
    hcf_ = 1
    if n1 > n2:
        k = n2
    else:
        k = n1
    for x in range(k, 2, -1):
        if(n1 % x == 0 and n2 % x == 0):
            hcf_ = x
            break
    print("HCF = ", hcf_)


HCF(36, 54)
# change the above numbers to
# find hcf of other numbers
