#BFS
graph = {
  '9' : ['6','8'],
  '6' : ['5', '7'],
  '8' : ['3'],
  '5' : [],
  '7' : ['3'],
  '3' : []
}

visited1 = [] 
queue = []     

def bfs(visited1, graph, node): 
  visited1.append(node)
  queue.append(node)

  while queue:          
    m = queue.pop(0) 
    print (m, end = ' ') 

    for neighbour in graph[m]:
      if neighbour not in visited1:
        visited1.append(neighbour)
        queue.append(neighbour)

#DFS
visited2 = set() 
def dfs(visited2, graph, node):  
    if node not in visited2:
        print (node, end = ' ')
        visited2.add(node)
        for neighbour in graph[node]:
            dfs(visited2, graph, neighbour)


print("Following is the Breadth-First Search")
bfs(visited1, graph, '9')

print("\nFollowing is the Depth-First Search")
dfs(visited2, graph, '9')

