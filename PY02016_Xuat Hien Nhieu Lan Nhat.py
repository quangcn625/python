
for __ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    Map = {}
    for i in a:
        if i in Map:
            Map[i] = Map.get(i) + 1
        else:
            Map[i] = 1
    Map = dict(sorted(Map.items(), key= lambda x :(-x[1], x[0])))
    ans = list(Map.items())[0]
    if ans[0] != 0 and ans[1] > n/2:
        print(ans[0])
    else:
        print('NO')

    
# 2
# 9
# 3 3 4 2 4 4 2 4 4
# 8
# 3 3 4 2 4 4 2 4