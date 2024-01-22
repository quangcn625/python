def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def is_krish_number(n):
    original_n = n
    digit_factorial_sum = 0
    
    while n > 0:
        digit = n % 10
        digit_factorial_sum += factorial(digit)
        n //= 10
    
    return digit_factorial_sum == original_n

if __name__ == '__main__':
    t = int(input())
    while t != 0:
        n = int(input())
        if is_krish_number(n):
            print("Yes")
        else:
            print("No")
        t = t - 1
