#FIND THE ACCESS CODES CHALLENGE
# Below I present two approaches but first (top) solution() function did not pass all the tests. As seen in the code the top code has a high running time
# O(n^3). This is due to itertools and creating all the combination of triples.
# The best solution, the bottom solution() function, is inspired by https://stackoverflow.com/questions/39846735/google-foobar-challenge-3-find-the-access-codes
# It is an elegant solution which does not rely on itertool library and the execution time is O(n^2).

#=============================first solution==========================#

import itertools

def solution1(l):
# THIS FUNCTION HAS HIGH RUNNING TIME O(N^3)
    # Create all possible triples
    triples = itertools.combinations(l, 3)
    print triples

    # Only keep ordered triples
    #sorted_triples = [x for x in triples if ((x[2]>=x[1]) and (x[1]>=x[0]))]

    # Only keep the ones where the third item is a multiple of the second
    lucky_triples = [x for x in triples if (x[2]%x[1] == 0)]

    # Only keep the ones where the second item is a multiple of the first
    lucky_triples_final = [x for x in lucky_triples if (x[1]%x[0] == 0)]

    #print(lucky_triples_final)

    return len(lucky_triples_final)

#=============================second solution==========================#

def solution(l):
    # Initializing a counter for every number in  the list
    counter = [0] * len(l)
    # Initializing a counter for number of triplets
    triplet_count = 0

    for i in range(0,len(l)): # i starts at 0 and stops before getting to length of l
        for j in range(0, i): # j starts at 0 and stops before getting to i

            if l[i] % l[j] == 0:
                print i, j
                #print l[i], l[j]
                # If a particular entry in the list has been a multiple of a previous number,
                # the counter for that entry increases
                counter[i] = counter[i] + 1

                #Each time we increment the counter, we can also increase our number of triplets by the factor
                # we're currently evaluating.
                triplet_count = triplet_count + counter[j]
                #print counter
    return triplet_count

print(solution([1, 2, 3, 4, 5, 6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]))
print(solution([1, 2, 4,8]))
print(solution2([1, 2, 3, 4, 5, 6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]))
