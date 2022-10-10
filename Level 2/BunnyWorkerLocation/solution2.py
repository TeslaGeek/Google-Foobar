# This solution is based on modeling in Excel i.e., regression analysis. It is a lot of fun to model in Excel if you have got time and curosity.  

#| 7
#| 4 8
#| 2 5 9
#| 1 3 6 10


def solution_equation(x, y):

    return str(int((0.5 * x*x)+(((y-1)+0.5)*x)+(0.5*y*y-1.5*y+1)))


print(solution_equation(100,20))
