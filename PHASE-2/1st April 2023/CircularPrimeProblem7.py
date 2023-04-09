#Problem7:
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def is_circular_prime(n):
    str_n = str(n)
    for i in range(len(str_n)):
        rotated = str_n[i:] + str_n[:i]
        if not is_prime(int(rotated)):
            return False
    return True

def count_circular_primes(limit):
    count = 0
    for i in range(2, limit):
        if is_circular_prime(i):
            count += 1
    return count

limit = int(input("Enter the limit: "))
count = count_circular_primes(limit)
print(f"The number of circular primes less than {limit} is {count}")
