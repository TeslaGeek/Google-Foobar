# Given a minion ID as a string n representing a nonnegative integer of length k in base b, where 2 <= k <= 9 and 2 <= b <= 10, 
# write a function solution(n, b) which returns the length of the ending cycle of the algorithm above starting with n. 
# For instance, in the example above, solution(210022, 3) would return 3, since iterating on 102212 would return to 210111 when done in base 3. 
# If the algorithm reaches a constant, such as 0, then the length is 1.

# The solution below is not complex. With some knowledge in sorting lists, strings, and base conversion the solution can be written in many ways but 
# the trick is watching the execution time and finding an optimal / minimal approach.

def solution(n, b):
    # I realized that foobar does not care for boundary checks as below hence the code is commented. 
    # Also I/O commands are not accepted such as print. They are helpful features though for debugging the code!
    
    #if str(n) == "":
    #    print("The number cannot be empty.\n")
    #    exit()
    #if not str(n).isdigit():
    #    print("The number does not contain digits between 0 and 9.\n")
    #    exit()

    #if b < 2 | b > 10:
    #    print("b is not the correct base i.e. 2<=b<=10.\n")
    #    exit()

    k = len(n)

    #if k < 2 | k > 9:
    #    print("The length of number is not sufficient i.e. 2<= the length of n <=9.\n")
    #    return 0;

    zlist = []
    while True:
        x = ''.join(sorted(n, reverse=True))
        #print x
        y = ''.join(sorted(n))
        #print y
        z10 = int(x, b) - int(y, b) # returns the integer in a given base to a decimal
        #print z10

        if b != 10:
            n = toBaseN(z10, b)
        else:
            n = str(z10)

        if len(zlist) < k:
            n = n.zfill(k)

        if n in zlist:
            return len(zlist) - zlist.index(n)
        zlist.append(n)


def toBaseN(num, b):
    baseNnum = []
    while num:
        baseNnum.insert(0, str(num % b))
        num = num // b
    #print "in the baseline", baseNnum
    return ''.join(baseNnum)


print(solution('1211', 10))  # => 1
print(solution('210022', 3))  # => 3

