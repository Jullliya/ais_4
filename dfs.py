n = int(input("Enter the count of points in graph: "))
pair = []
m = int(input("Enter the number of pairs: "))
print("Enter the pair of point: ")
for i in range(m):
    pair.append([int(x) for x in input().split()])

g = []
for i in range(n):
    g.append([0]*n)

start = int(input("Enter the start point: ")) - 1
visited = [False] * (n + 1)
prev = [-1] * (n + 1)

for i in range(m):
    g[pair[i][0]-1][pair[i][1]-1] = 1

def dfs(start, visited, prev, g):
    visited[start] = True
    for u in range(len(g[start])):
        if not visited[u] and g[start][u]:
            prev[u] = start
            dfs(u, visited, prev, g)

dfs(start, visited, prev, g)
for i in range(len(prev)):
    if prev[i] != -1:
        print(prev[i]+1, "->", i + 1)