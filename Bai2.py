# Nhập thông tin của danh sách học sinh
def DanhSach():
    a = []
    soSV = int(input())
    for i in range(soSV):
        name = input()
        dob = input()
        diemTB = input()
        
        sinh_vien = f"{name}\t{dob}\t{diemTB}"
        a.append(sinh_vien)
    return a

# Ghi thông tin vào tệp danhsach.txt
def Ghi(a):
    try:
        with open("danhsach.txt", "w") as file:
            soSV = len(a)
            file.write(f"{soSV}\n")
            for sinhvien in a:
                file.write(f"{sinhvien}\n")
    except Exception as e:
        return None

# Tìm thông tin của sinh viên có điểm trung bình cao nhất
def DiemCaoNhat():
    try:
        with open("danhsach.txt", "r") as file:
            lines = file.readlines()
            diemMax = 0
            thongtinSV = ""
            for line in lines[1:]:
                info = line.split("\t")
                diemTB = float(info[2])
                if diemTB > diemMax:
                    diemMax = diemTB
                    thongtinSV = line
            return thongtinSV.strip()
    except Exception as e:
        return None

# Nhập danh sách học sinh và ghi vào tệp
danhsach = DanhSach()
ghitep = Ghi(danhsach)

# Tìm sinh viên có điểm cao nhất và in thông tin ra màn hình
print(f"Thông tin của sinh viên có điểm trung bình cao nhất là: {DiemCaoNhat()}")

