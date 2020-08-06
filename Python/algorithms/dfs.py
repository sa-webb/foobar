'''
Depth First Search Full Traveral
'''
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

graph2 = {'A': ['B', 'C'],
          'B': ['A', 'D', 'E'],
          'C': ['A', 'F'],
          'D': ['B'],
          'E': ['B', 'F'],
          'F': ['C', 'E']}

visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print('Visiting ', node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)


dfs(visited, graph, 'A')
# graph = {A,B,D,E,F,C}
# graph2 = {A,B,D,E,F,C}
