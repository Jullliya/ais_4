# введем значение размерности графа
n = int(input("Enter the count of points in graph: "))
pair = []
# введем количество пар соединенных вершин
m = int(input("Enter the number of pairs: "))
# введем пары соединений вершин
print("Enter the pair of point: ")

for i in range(m):
    pair.append([int(x) for x in input().split()])

g = []
for i in range(n):
    g.append([0]*n)

# ввод необходимых значений
path, start, end = 0, 0, 0
while start > n-1 or start <= 0:
    start = int(input("Enter the start point: ")) - 1
    if start > n-1:
        print("Incorrect value of start number, start more than graph dimensions.")
    if start < 0:
        print("Incorrect value of start number, start cannot be negative or zero. ")
while end > n-1 or end <= 0:
    end = int(input("Enter the last point: ")) - 1
    if end > n-1:
        print("Incorrect value of start number, end more than graph dimensions.")
    if end < 0:
        print("Incorrect value of start number, end cannot be negative or zero. ")
visited = [False] * (n + 1)
prev = [-1] * (n + 1)

# преобразователь парных значений координат в матрицу
for i in range(m):
    g[pair[i][0]-1][pair[i][1]-1] = 1

# функция обхода графа в глубину с подсчетом длины маршрута
def dfs(start, end, visited, prev, g, path):
    visited[start] = True
    for u in range(len(g[start])):
        if not visited[u] and g[start][u] and u != end:
            path = path + 1
            prev[u] = start
            dfs(u, end, visited, prev, g, path)
    return path

# вызов функции
print(dfs(start, end, visited, prev, g, path))