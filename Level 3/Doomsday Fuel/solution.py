# PASSED ALL THE TESTS.
#
# EXCELLENT TUTORIAL IN
#   https://github.com/ivanseed/google-foobar-help/blob/master/challenges/doomsday_fuel/doomsday_fuel.md
#    and https://en.wikipedia.org/wiki/Absorbing_Markov_chain
#    Steps taken to calculate the probability matrix for terminal states
#    (1) Order the matrix so that rows start with terminal states first.Sort the columns correctly to
#    reflect this so everything matches up.
#    (2) Now that you have done that you know how to find R and Q.
#    (3) Calculate F=(I-Q)^-1
#    (4) Calculate F*R.
#    (5) Get the first line of FR and then you have your probabilities.
#    (6) Find the common denominator and return the int array how the specification has asked it to be formatted.
#
#       THIS HAS BEEN MY FAVOURITE CHALLENEGE SO FAR. I have a background in robotics and absorbing Markov chains are important in leading
#       a robotic arm to a stable state (terminal state).

from fractions import Fraction
from fractions import gcd


def fraction(numerator, denominator=1):
    return 0 if numerator == 0 else Fraction(numerator, denominator)

def subtract(a, b):
    # subtract matrix b from a
    n = xrange(len(a))
    return [[a[i][j] - b[i][j] for j in n] for i in n]

def identity(m):
    # identity matrix for matrix m
    n = xrange(len(m))
    return [[1 if i == j else 0 for j in n] for i in n]

def multiply(a, b):
    # multiply matrices a x b
    return [[sum(i * j for i, j in zip(r, c)) for c in zip(*b)] for r in a]

def invert(a):
    # https://github.com/ThomIves/MatrixInverse/blob/master/MatrixInversion.py
    b = identity(a)
    for d in xrange(len(a)):
        to1 = fraction(1, a[d][d])
        for j in xrange(len(a)):
            a[d][j] *= to1
            b[d][j] *= to1
        for i in range(len(a))[0:d] + range(len(a))[d + 1 :]:
            to0 = a[i][d]
            for j in xrange(len(a)):
                a[i][j] = a[i][j] - to0 * a[d][j]
                b[i][j] = b[i][j] - to0 * b[d][j]
    return b

def lcm(a):
    # least common multiple for array
    for i, x in enumerate(a):
        lcm = x if i == 0 else lcm * x // gcd(lcm, x)
    return lcm

def solution(m):
    """
    This problem describes an absorbing Markov Chain.
    https://en.wikipedia.org/wiki/Absorbing_Markov_chain
    The provided data is almost in canonical form, P.  With this matrix,
    we can then use its properties to determine B, the probabilities of
    ending up in a particular absorbing (terminal) state.
              _       _
             |         |
             |  Q   R  |
        P =  |         |
             |  0   I  |
             |_       _|

        F =   ( I - Q) ^ -1

        FR =  F * R
    """

    terminal = [not any(row) for row in m]

    if terminal.count(True) == 1:
        return [1, 1]

    p = [
        [
            1
            if terminal[state] and state == next_state
            else fraction(prob, sum(m[state]))
            for next_state, prob in enumerate(probs)
        ]
        for state, probs in enumerate(m)
    ]

    q = [
        [p[i][j] for j, is_terminal in enumerate(terminal) if not is_terminal]
        for i, is_terminal in enumerate(terminal)
        if not is_terminal
    ]

    r = [
        [p[i][j] for j, is_terminal in enumerate(terminal) if is_terminal]
        for i, is_terminal in enumerate(terminal)
        if not is_terminal
    ]

    # probabilities for starting in state 0
    fr0 = multiply(invert(subtract(identity(q), q)), r)[0]

    common = lcm([x.denominator for x in fr0])

    return [x.numerator * common / x.denominator for x in fr0] + [common]

print(solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
print(solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]))
