def solve(a):
    sum = 0
    while a > 0:
        sum = sum + a % 10
        a //= 10
    return sum
def cmp(a):
    return (solve(a),a)

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = int(input())
        a = [int(i) for i in input().split()]
        a = sorted(a,key=cmp)
        a = ' '.join(str(i) for i in a)
        print(a)
        t -= 1