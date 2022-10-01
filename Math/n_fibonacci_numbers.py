# Fibonacci Sequence is a very famous series in Mathematics
# Each Term in this series is made from the sum of previous two terms
# The series starts from 0 and 1
# So 0 1 then their sum is 1 so third term is 1
# This series continues as 0 1 1 2 3 ......


def FibonacciPrinter(n):
    # Here we initialize the first two terms as 0 and 1.
    n1, n2 = 0, 1

    # This counter counts the number of terms
    counter = 0

    if n == 1:
        print(n1)

    else:
        # The while loop runs till counter exceeds number of terms n
        while counter < n:
            print(n1, end=" ")

            # nth term is the sum of previous two terms
            nth = n1 + n2

            # For the next iteration, the second term becomes first term
            n1 = n2

            # and the term calculated now is the second term
            n2 = nth

            # counter is updated as the terms are increased
            counter = counter + 1


FibonacciPrinter(7)
