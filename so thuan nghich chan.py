def check (n):
    for i in range(len(n)):
        if int(n[i]) % 2 != 0: 
            return False
    return True

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        N = input()
        n = 0
        while True:
            n += 2
            res = str(n)
            if check(res):
                reverse = res[::-1]
                res = res + reverse
                if int(res) >= int(N): 
                    break
                print (res, end=" ")
        print()