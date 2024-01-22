
class ToaDo:
    def __init__(self, start, finish):
        self.start = start
        self.finish = finish

for __ in range(int(input())):
    n = int(input())
    a = []
    for i in range(n):
        x, y = map(int, input().split())
        a.append(ToaDo(x, y))
    a.sort(key= lambda x : x.finish)
    cnt = 1
    i = 0
    for j in range(1, n):
        if a[i].finish <= a[j].start:
            i = j
            cnt += 1
    print(cnt)


# 1
# 10
# 39 55
# 37 74
# 0 1
# 19 25
# 65 76
# 51 52
# 19 21
# 5 94
# 46 65
# 32 40
    