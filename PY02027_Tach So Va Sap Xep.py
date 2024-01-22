
a = []
for __ in range(int(input())):
    s = input() + '#'
    ans = 0
    check = 0
    for i in s:
        if i.isdigit():
            check = 1
            ans = ans * 10 + int(i)
        else:
            if check == 1:
                a.append(ans)
                ans = 0
                check = 0
a.sort()
for i in a:
    print(i)

# 3
# A129h
# G07bxjq3
# aaaaaaa4aaaa

        
    