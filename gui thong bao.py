for i in range(int(input())):
    list = [i for i in input().split()]
    cnt = 0
    for i in list:
        if cnt + len(i) > 100:
            break
        print(i,end='')
        cnt += len(i)
        print(end=' ')
        cnt += 1
    print()




#Can cu Ke hoach giang day – hoc tap hoc ky 1 nam hoc 2021 – 2022 Can cu ket qua thi hoc ky 2 va hoc ky phu ky he nam hoc 2020 – 2021