
n = int(input())
a, b= [], []
while len(a) < n:
    a.extend(input().split())
for i in a:
    b.append(int(i))

Max = max(b)
check = 0
for i in range(1, Max + 1):
    if i not in b:
        check = 1
        print(i)
if check == 0:
    print('Excellent!')

