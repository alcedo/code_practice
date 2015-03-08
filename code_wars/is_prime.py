__author__ = 'vic'


"""Wikipedia sieve explanation:
To find all the prime numbers less than or equal to a given integer n by Eratosthenes' method:

Create a list of consecutive integers from 2 through n: (2, 3, 4, ..., n).
Initially, let p equal 2, the first prime number.
Starting from p, enumerate its multiples by counting to n in increments of p, and mark them in the list (these will be 2p, 3p, 4p, ... ; the p itself should not be marked).
Find the first number greater than p in the list that is not marked. If there was no such number, stop. Otherwise, let p now equal this new number (which is the next prime), and repeat from step 3.
"""


def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True

    sieve = range(num + 1)
    p = 2  # first prime number
    marker = 2
    mark_list = []
    prime_list = []
    found = False
    while not found:
        while (marker * p) <= num:
            mark_list.append(marker * p)
            marker += 1
        prime_list.append(p)

        # find first p that isnt marked
        for s in sieve:
            if s > p and s not in mark_list:
                p = s
                found = False
                break
            else:
                found = True

        marker = 2

    print prime_list
    return num in prime_list


is_prime(11)