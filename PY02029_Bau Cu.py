
n, m = map(int, input().split())
x = input().split()
a = []
if len(x) == n:
    a = [int(i) for i in x]
Map = {}
for i in a:
    if i in Map:
        Map[i] = Map.get(i) + 1
    else:
        Map[i] = 1

# dict ép về kiểu map
Map = dict(sorted(Map.items(), key= lambda x : (-x[1], x[0])))
Max = list(Map.values())[0]
check = 0
for k, v in Map.items():
    if v < Max:
        check = 1
        print(k)
        break
if check == 0:
    print('NONE')




# 11 4
# 2 3 1 2 3 4 1 2 3 2 1
# 8 4
# 1 2 3 4 4 3 2 1