
"""
The aim is to figure out
the most efficient way to sort
and shift the pellets down to a single pellet at a time.

To do it efficiently I have assumed it is best to minimise
the number of counts. I noticed if the process gets to 5,
increasing the number of pellets to 6 increases the count
by 1, however decresing the number of pellets to 4 decreases
the count by 1, which is more efficient.

"""

def solution(n):
    # count min number of add/subtract/halve operations to reach 1
    n = int(n)  # assume we use base 10
    count = 0
    while n != 1:
        if n % 2:  # odd
            if n % 4 == 1 or n == 3: # checking for 5 or 3 in the process
                n -= 1  # subtract is better
            else:
                n += 1  # otherwise add
        else:  # even, halve
            n /= 2
        count += 1
    return count

print solution(15)
print solution(5)
print solution(3)
