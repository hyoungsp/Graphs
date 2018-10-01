'''
Python Code for Union-Find: using DFS Recursion
'''

from collections import defaultdict

parent = defaultdict(int)

## initialize the parent of each vertex is itself
for i in range(1, 11):
    parent[i] = i

## DFS (recursively find out which vertex is a parent vertex)
def get_parent(vertex):
    if parent[vertex] == vertex:
        return vertex
    return get_parent(parent[vertex])

## We are connecting two different vertex with an edge
def union_parent(vertex1, vertex2):
    parent_v1 = get_parent(vertex1)
    parent_v2 = get_parent(vertex2)
    if parent_v1 < parent_v2:
        parent[vertex2] = vertex1
    else:
        parent[vertex1] = vertex2

## Boolean value for checking if the two vertices are in a same graph
def in_sameGraph(vertex1, vertex2):
    vertex1 = get_parent(vertex1)
    vertex2 = get_parent(vertex2)
    if vertex1 == vertex2:
        return True, "Yes, they are in a same graph"
    return False, "No, they are not"

'''
Suppose there are 10 different vertex (initially)
and connext vertex 1 ~ 4 and vertex 5 ~ 6

then, check if vertex 1 and vertex 5 are in a same graph (>> expected False)
and after we see if the result would change if we connect vertex 4 and 5
'''
union_parent(1, 2)
union_parent(2, 3)
union_parent(3, 4)

union_parent(5, 6)
union_parent(6, 7)
union_parent(7, 8)

print("Are vertex 1 and vertex 5 in a same Graph?")
print(in_sameGraph(1, 5)[1])

union_parent(4, 5)

print("Are vertex 1 and vertex 5 in a same Graph?")
print(in_sameGraph(1, 5)[1])