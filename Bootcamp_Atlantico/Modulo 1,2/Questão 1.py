def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes(numbers):
    prime_numbers = []
    for number in numbers:
        if is_prime(number):
            prime_numbers.append(number)
    return prime_numbers

input_str = input("Digite uma lista de números separados por espaço: ")
numeros = [int(x) for x in input_str.split()]
primos = find_primes(numeros)
print(primos)
