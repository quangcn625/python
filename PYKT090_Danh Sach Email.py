
f = open('CONTACT.in', 'r')
List = []
for i in f:
    tmp = ''
    for j in i:
        if j.isalpha():
            tmp += j.lower()
        else:
            tmp += j
    if tmp not in List:
        List.append(tmp)
List.sort()
print(*List, sep='\n')