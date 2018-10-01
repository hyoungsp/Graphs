'''
Using DFS -> return sequence of graph nodes in topological order

a 
 \
  \ --> d---> e
  /           ^
 /             \
b               c

1) d cannot be done before a and b are done
2) e cannot be done before c and d are done

'''

from collections import defaultdict, deque

adj_list = defaultdict(list)

## adjacency list of each graph nodes
adj_list['a'] = ['d']
adj_list['b'] = ['d']
adj_list['d'] = ['e']
adj_list['c'] = ['e']
adj_list['e'] = []

visited = {}
visited['a'] = False
visited['b'] = False
visited['c'] = False
visited['d'] = False
visited['e'] = False

# Store the result order of graph nodes through topological sort
topological_sort_result = deque()

def topological_sort(vertex):
    if not visited[vertex]:
        visited[vertex] = True
        for neighbor in adj_list[vertex]:
            topological_sort(neighbor)
        ## can also use just list but try to avoid reverse when done > using queue
        topological_sort_result.appendleft(vertex)


for vertex in visited:
    topological_sort(vertex)

print(topological_sort_result)

## ['c', 'b', 'a', 'd', 'e']
