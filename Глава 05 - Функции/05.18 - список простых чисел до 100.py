import prime_numbers_05_17

def main():
    prime_numbers = [n for n in range (1, 101) if prime_numbers_05_17.is_prime(n)]
    print(prime_numbers)

main()
