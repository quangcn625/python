def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

def prime_factors_sum(numbers):
    prime_factors_sum = 0
    for number in numbers:
        factors = prime_factors(number)
        prime_factors_sum += sum(factors)
    return prime_factors_sum

# Đọc vào danh sách các số nguyên từ người dùng
n = int(input())
numbers = []
for i in range(n):
    num = int(input())
    numbers.append(num)

total_prime_factors_sum = prime_factors_sum(numbers)
print(total_prime_factors_sum)
