# This challenge is related to data structures and in partciular graph data structures.
# if unfamilar with graph data structures this website is a great resource: https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/?ref=lbp
# To solve this challenge I had to remind myself about different search methods in graphs: breadth first search (BFS) vs depth first search (DFS).
# Then I started reading on max flow problem https://www.geeksforgeeks.org/max-flow-problem-introduction/ and various methods proposed to solve the
# max flow problem. It is an interesting problem space with great solutions proposed by Ford-Fulkerson (https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/)
# and Dinic (https://www.geeksforgeeks.org/dinics-algorithm-maximum-flow/). Alhtough the outcomes of both algorithms are identical, Dinic's is more time
# efficient and knowing how Foobar codes are assessed (low execution time is preferred), I opted for Dinic's algorithm.
#
# The essence of Dinic's algorithm is:

# * A flow is maximum if there is no s to t path in residual graph.
# * BFS is used in a loop. There is a difference though in the way we use BFS in both algorithms
# (Ford-Fulkerson and Dinic).
#
# In Ford-Fulkerson`s algorithm, we use BFS to find an augmenting path and send flow across this path. In Dinic`s
# algorithm, we use BFS to check if more flow is possible and to construct level graph.
# In level graph, we assign levels to all nodes, level of a node is shortest distance (in terms of number of edges) of
# the node from source. Once level graph is constructed, we send multiple flows using this level graph.
# This is the reason it works better than Ford-Fulkerson. In Ford-Fulkerson, we send only flow that is send across the
# path found by BFS.

# Outline of Dinic`s algorithm :
#
# Initialize residual graph G as given graph.
# Do BFS of G to construct a level graph (or assign levels to vertices) and also check if more flow is possible.
# If more flow is not possible, then return
# Send multiple flows in G using level graph until blocking flow is reached.
# Here using level graph means, in every flow, levels of path nodes should be 0, 1, 2 ... (in order) from s to t.
# I re-used the BFS algorithm in https://www.geeksforgeeks.org/dinics-algorithm-maximum-flow/ and worked on the rest of
# the solution as below.
#
# The code below passed all the tests on the Foobar. This is a non trivial challenge for sure and almost took 12 days
# (out of assigned 14 days) to complete.


def bfs(matrix, source, destination):
    visited = [-1 for i in range(len(matrix))]
    visited[source] = source
    queue = [source]
    while len(queue) > 0:
        top = queue.pop(0)
        for i in range(len(matrix)):
            if (matrix[top][i][1] - matrix[top][i][0]) != 0 and visited[i] == -1:
                if i == destination:
                    # Get route
                    visited[destination] = top
                    path = [destination]
                    temp = destination
                    while temp != source:
                        temp = visited[temp]
                        path.append(temp)
                    path.reverse()
                    # Get flow value and update augmented graph
                    temp = 1
                    total = float("inf")
                    cur = source
                    while temp != len(path):
                        entry = matrix[cur][path[temp]]
                        diff = abs(entry[1]) - entry[0]
                        total = min(total, diff)
                        cur = path[temp]
                        temp += 1
                    temp = 1
                    cur = source
                    while temp != len(path):
                        entry = matrix[cur][path[temp]]
                        if entry[1] < 0: # Already augmented need to flip
                            entry[1] += total
                        else:
                            entry[0] += total
                        entry = matrix[path[temp]][cur]
                        if entry[1] <= 0: # Already augmented need to flip
                            entry[1] -= total
                        else:
                            entry[0] += total
                        cur = path[temp]
                        temp += 1
                    return True
                else:
                    visited[i] = top
                    queue.append(i)
    return False

def solution(entrances, exits, path):
    max_val = sum(list(map(sum, path)))
    aug = []
    for i in range(len(path)):
        aug.append([])
        for j in range(len(path[i])):
            aug[i].append([0, path[i][j]])
        aug[i].append([0, 0])
        if i in exits:
            aug[i].append([0, max_val])
        else:
            aug[i].append([0, 0])
    aug.append([])
    aug.append([])
    for i in range(len(path[0]) + 2):
        if i in entrances:
            aug[-2].append([0, max_val])
        else:
            aug[-2].append([0, 0])
        aug[-1].append([0, 0])
    while bfs(aug, len(aug)-2, len(aug)-1):
        pass
    total = 0
    for i in range(len(aug)):
        total += aug[-2][i][0]
    return total

print(solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]))
print(solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
