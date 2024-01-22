def solve(S, N):
    count = 0
    n_str = str(N)  # Chuyển số N thành chuỗi để dễ so sánh từng chữ số

    i = 0
    while i < len(S):
        if S[i] == n_str[0]:
            j = 1
            while j < len(n_str) and i + j < len(S) and S[i + j] == n_str[j]:
                j += 1

            if j == len(n_str):
                count += 1
                i += j  # Tiến tới vị trí sau khi tìm thấy số N
            else:
                i += 1
        else:
            i += 1

    return count

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        s = input()
        n = int(input())
        print(solve(s,n))
        t -= 1
