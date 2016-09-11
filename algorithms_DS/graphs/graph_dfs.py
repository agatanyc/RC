"""Visit every node in a graph. Try both bfs and dfs methods."""

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def dfs(graph, start):
    visited = set()
    stack = [start]
    while stack:
        n = stack.pop()
        if n not in visited:
            visited.add(n)
            for v in graph[n]:
                stack.append(v)
    return visited

assert dfs(graph, 'B') == set(['A', 'C', 'B', 'E', 'D', 'F'])

def bfs(graph, start):
    visited = set()
    queue = [start]
    while queue:
        n = queue.pop(0)
        if n not in visited:
            visited.add(n)
            for v in graph[n]:
                queue.append(v)
    return visited

assert bfs(graph, 'B') == set(['A', 'C', 'B', 'E', 'D', 'F'])

    
