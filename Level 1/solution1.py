
# Write a function called solution(data, n) that takes in a list of less than 100 integers and a number n,
# and returns that same list but with all of the numbers that occur more than n times removed entirely.
# The returned list should retain the same ordering as the original list - you don't want to mix up those
# carefully-planned shift rotations! For instance, if data was [5, 10, 15, 10, 7] and n was 1, solution(data, n)
# would return the list [5, 15, 7] because 10 occurs twice, and thus was removed from the list entirely.

# The solution below uses dictionary and two nested loops. The execution time is O(n^2) and I strongly assume this was the reason behind failing 
# two hidden tests when I uploaded to the server, the code works fine on the given test cases though.

def solution(data, n):
    # Your code here

    if len(data) < 100:
        count = dict()
        for i in data:
          count.setdefault(i, 0)
          count[i] += 1
    
        for k, v in count.items():
          if v > n:
            for i in range(v):
                data.remove(k)
    return data
  
  
print (solution([5,10,17,10,7],1))
print (solution([1,2,3],0))
print (solution([1,2,3,1,2,3],0))
print (solution([1, 2, 2, 3, 3, 3, 4, 5, 5],1))
