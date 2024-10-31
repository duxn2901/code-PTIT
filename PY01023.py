prime_list = [2]

dct = {}

def is_prime(n):
    n = int(n)
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True


def add_lower_primes(n):
    for i in range(3,n,2):
        if is_prime(i):
            prime_list.append(i)


def divide_num(n):
    if n == 1:
        return True

    for i in prime_list:

        if n % i == 0:
            if i in dct:
                dct[i] += 1
            else:
                dct[i] = 1
            n //= i
            print(n)
            return divide_num(n)








testcases = int(input())
test_list =[]
for _ in range(testcases):
    test_list.append(int(input()))
add_lower_primes(max(test_list))
for i in test_list:
    divide_num(i)
print(dct)



