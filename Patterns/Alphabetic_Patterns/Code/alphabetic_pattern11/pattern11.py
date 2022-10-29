# code for alphabeticpattern11

# outerloop

for i in range(ord('E'), ord('A')-1, -1):
    # innerloop
    for j in range(ord('E'), i-1, -1):
        print(chr(j), end="")
    print()
