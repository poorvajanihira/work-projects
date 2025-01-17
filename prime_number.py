def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def print_primes(limit):
    for num in range(2, limit + 1):
        if is_prime(num):
            print(num)

# Example usage:
limit = 50  # Replace with your desired limit
print_primes(limit)