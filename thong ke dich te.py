
n, m = map(int, input().split())
a = []
for _ in range(n):
    row = list(map(int, input().split()))
    a.append(row)

visited = [[False for _ in range(105)] for _ in range(105)]

dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [1, 1, 1, 0, 0, -1, -1, -1]

ans = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == -1:
            for k in range(8):
                x = i + dx[k]
                y = j + dy[k]
                if 0 <= x < n and 0 <= y < m and not visited[x][y]:
                    ans += a[x][y]
                    visited[x][y] = True

print(ans)
