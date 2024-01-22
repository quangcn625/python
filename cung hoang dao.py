t = int(input())

while t != 0:
    x,y = map(int,input().split())
    if (x >= 21 and y == 3) or (x <= 19 and y == 4):
        print("Bach Duong")
    elif (x >= 20 and y == 4) or (x <= 20 and y == 5):
        print("Kim Nguu")
    elif (x >= 21 and y == 5) or (x <= 20 and y == 6):
        print("Song Tu")
    elif (x >= 21 and y == 6) or (x <= 22 and y == 7):
        print("Cu Giai")
    elif (x >= 23 and y == 7) or (x <= 22 and y == 8):
        print("Su Tu")
    elif (x >= 23 and y == 8) or (x <= 22 and y == 9):
        print("Xu Nu")
    elif (x >= 23 and y == 9) or (x <= 22 and y == 10):
        print("Thien Binh")
    elif (x >= 23 and y == 10) or (x <= 22 and y == 11):
        print("Thien Yet")
    elif (x >= 23 and y == 11) or (x <= 21 and y == 12):
        print("Nhan Ma")
    elif (x >= 22 and y == 12) or (x <= 19 and y == 1):
        print("Ma Ket")
    elif (x >= 20 and y == 1) or (x <= 18 and y == 2):
        print("Bao Binh")
    elif (x >= 19 and y == 2) or (x <= 20 and y == 3):
        print("Song Ngu")

    t = t - 1

