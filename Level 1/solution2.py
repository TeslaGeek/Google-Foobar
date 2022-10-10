# Write a function called solution(data, n) that takes in a list of less than 100 integers and a number n,
# and returns that same list but with all of the numbers that occur more than n times removed entirely.
# The returned list should retain the same ordering as the original list - you don't want to mix up those
# carefully-planned shift rotations! For instance, if data was [5, 10, 15, 10, 7] and n was 1, solution(data, n)
# would return the list [5, 15, 7] because 10 occurs twice, and thus was removed from the list entirely.

#This solution is minimalist and its completion time is O(n). It uses .count function to count the number of repetition in each set of data and if the 
# count is more than one, it will discard the number otherwise it will append to the empty result list.

def solution(data, n):
    # Your code here

    results = []
    if len(data) < 100:
        for d in data:
            if n <= 1:
                if data.count(d) > n:
                    pass
                elif data.count(d) == n:
                    results.append(d)
            elif n > 1:
                if data.count(d) >= n:
                    pass
                elif data.count(d) < n:
                    results.append(d)
    return results

  
print (solution([5,10,17,10,7],1))
print (solution([1,2,3],0))
print (solution([1,2,3,1,2,3],0))
print (solution([1, 2, 2, 3, 3, 3, 4, 5, 5],1))


