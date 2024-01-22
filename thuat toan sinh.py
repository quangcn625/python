n = int(input())

sum = 1

for i in range(2,n,1):
    if n % i == 0:
        sum += i
if sum > n :
    print("True")

else:
    print("False")