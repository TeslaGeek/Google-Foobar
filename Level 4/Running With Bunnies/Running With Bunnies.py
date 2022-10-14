# This challenge is related to graph data structures in particular the ones
# with negative cycles (or negative weight edges).
# if unfamilar with graph data structures this website is a great resource: https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/?ref=lbp
#
# To solve graphs with cycles there are various solutions including Dijkstra and Bellman-Ford. However, Dijkstra
# does not work for graphs with negative cycles. So to solve this challenge I used Bellman-Ford algorith
# https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/
#
# In summary the algorithm finds the shortest distance to all vertices from the source. To do so:
#
# 1 - Initialize distances from the source to all vertices as infinite and distance to the source itself as 0.
#     Create an array dist[] of size |V| with all values as infinite except dist[src] where src is source vertex.
# 2- Calculate shortest distances.
#   Do following |V|-1 times where |V| is the number of vertices in given graph.
#       Do following for each edge u-v
#           If dist[v] > dist[u] + weight of edge uv, then
#                   update dist[v] to dist[v] = dist[u] + weight of edge uv
# 3- Report if there is a negative weight cycle in the graph.
#    Again traverse every edge and do following for each edge u-v
#       .... If dist[v] > dist[u] + weight of edge uv, then '''Graph contains negative weight cycle'''
#  The idea of step 3 is, step 2 guarantees the shortest distances if the graph doesn't contain a negative weight cycle.
#  If we iterate through all edges one more time and get a shorter path for any vertex, then there is a negative weight
#  cycle

from itertools import permutations

def bellmanFord(graph):
    distances = [] # we create a matrix for all vertices
    for vertex in range(len(graph)):
        distances.append(findDistance(graph,vertex))

    return distances

def findDistance(graph, src):
    n = len(graph)
    distance = [float('inf')] * n
    distance[src] = 0

    for i in range (n):
        for u in range (n):
            for v in range(n):
                weight = graph[u][v]
                if distance[u] + weight < distance [v]:
                    distance[v] = distance[u] + weight
    return distance

def negativeCycle(graph):
    distance = graph[0];
    n = len(graph)
    for u in range(n):
        for v in range(n):
            weight = graph[u][v]
            if distance[u] + weight < distance[v]:
                return True
    return False

def getPathTime(bunnies, graph):
    time = 0
    time += graph[0][bunnies[0]]
    time += graph[bunnies[-1]][len(graph) - 1]

    for i in range(1, len(bunnies)):
        u = bunnies[i-1]
        v = bunnies [i]
        time += graph[u][v]
    return time

def solution(times, times_limit):
    n_bunnies = len(times) - 2  # remaining count represent the bunnies
    bunnies = [x for x in range(1,n_bunnies+1)]

    #calculate the distance matrix
    distances = bellmanFord(times) #we pass the initial matrix times
    if negativeCycle(distances):
        return range(n_bunnies) #if we have negative cycle we can go back over and over and pick up the bunnies

    for i in range(n_bunnies, 0, -1):
        for perm in permutations(bunnies, i):
            time = getPathTime(perm,distances)
            if time <= times_limit:
                return [x-1 for x in sorted(perm)] # return bunnines ID in a sorted manner

    return[]

print(solution([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1))

print (solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3))
