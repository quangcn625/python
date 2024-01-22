def is_valid(matrix, x, y, size):
    # Kiểm tra xem ma trận con có hợp lệ hay không
    for i in range(size):
        for j in range(size):
            if matrix[x + i][y + j] != 1:
                return False
    return True

def count_submatrices_with_sum_K(A, K):
    if not A:
        return 0

    rows, cols = len(A), len(A[0])
    count = 0

    for size in range(1, min(rows, cols) + 1):
        for i in range(rows - size + 1):
            for j in range(cols - size + 1):
                if is_valid(A, i, j, size):
                    # Tính tổng các phần tử của ma trận con và kiểm tra có bằng K không
                    submatrix_sum = sum(A[i + x][j + y] for x in range(size) for y in range(size))
                    if submatrix_sum == K:
                        count += 1

    return count

# Để sử dụng hàm trên:
A = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
]
K = 2
result = count_submatrices_with_sum_K(A, K)
print("Số lượng ma trận đơn vị con có tổng các phần tử bằng", K, "là:", result)
