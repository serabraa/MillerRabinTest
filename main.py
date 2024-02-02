import random

##Tested on 53(prime),561(not prime),7817(prime),100000(not prime)
def miller_rabin_test(n, round =5):

    if n == 2 or n == 3:
        return True

    if n <= 1 or n % 2 == 0:
        return False

    ##(n - 1) as 2^k * m form
    k, m = 0, n - 1
    while m % 2 == 0:
        k += 1
        m //= 2

    for _ in range(round):
        a = random.randint(2, n - 2)
        x = pow(a, m, n)  # Compute a^d % n

        if x == 1 or x == n - 1:
            continue

        for _ in range(k - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True


num = int(input("Enter a number to test for primality: "))
if miller_rabin_test(num):
    print(f"{num} is probably prime.")
else:
    print(f"{num} is composite.")
