def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

angka = int(input("Masukin angka: "))
print(f"{angka} prima") if is_prime(angka) else print(f"{angka} bukan prima")
