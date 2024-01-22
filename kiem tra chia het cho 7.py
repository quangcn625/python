def solve(a):
    ans = 0
    while a > 0:
        ans = ans * 10 + int(a % 10)
        a = a // 10
    return ans

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = int(input())
        m = 1000
        ans = 0
        flag = 0
        if n % 7 == 0:
            flag = 1
            print(n)
        else:
            while m != 0:
                ans = ans + n
                x = solve(n)
                ans = ans + x
                if ans % 7 == 0:
                    flag = 1
                    print(ans)
                    break
                else:
                    n = ans
                    ans = 0
                    m -= 1
        if flag == 0:
            print(-1)
        t -= 1