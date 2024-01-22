def check(a):
    b = a
    ans = 0
    cnt = 0
    while a > 0:
        cnt = cnt + 1
        ans = ans * 10 + int(a % 10)
        a = int(a / 10)
    if cnt > 1 and b == ans:
        return True
    return False

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        s = input()
        sum = 0
        for i in range(len(s)):
            sum = sum + int(s[i])
        if check(sum) == True:
            print("YES")
        else:
            print("NO")
        
        t -= 1