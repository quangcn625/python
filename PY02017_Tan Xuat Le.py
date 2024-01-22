
for __ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    Map = {}
    for i in a:
        if i in Map:
            Map[i] = Map.get(i) + 1
        else:
            Map[i] = 1
    for k, v in Map.items():
        if v % 2 != 0:
            print(k)
            break

# 2
# 7
# 1 2 3 2 3 1 3
# 5
# 1 1 3 3 2