# I propose two solutions: one conventional array indexing and finding the ID and the next in solution2.py using a function to model the triangle.
# The solution below requires a bit of creative thinking otherwise it is not a difficult one to program. 

def solution(x, y):
    xIndex, yIndex, workerId = 1, 1, 1

    while xIndex < x:
        xIndex += 1
        workerId += xIndex

    while yIndex < y:
        yIndex += 1
        workerId += xIndex
        xIndex += 1

    return str(workerId)

#| 7
#| 4 8
#| 2 5 9
#| 1 3 6 10

print(solution_equation(100,20))
