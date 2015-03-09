# Question:
# Return the sum of all multiples of 3 and 5 below a number

# http://rosettacode.org/wiki/Sum_multiples_of_3_and_5#Python
# this sounds like a fizzbuzz question
# Simple
# def solution(number):
# sum = 0
#   for i in xrange(number):
#     if i % 3 == 0:
#       sum += i
#     elif i % 5 == 0:
#       sum += i
#   return sum


def solution(n):
    return sum(range(3, n, 3)) + sum(range(5, n, 5)) - sum(range(15, n, 15))


def sum35c(n):
    'Sum the arithmetic progressions: sum3 + sum5 - sum15'
    consts = (3, 5, 15)
    # Note: stop at n-1 because want the sum of multiples to be below n as stated
    # in the above question
    # // is a floor division symbol
    divs = [(n - 1) // c for c in consts]
    sums = [d * c * (1 + d) / 2 for d, c in zip(divs, consts)]
    return sums[0] + sums[1] - sums[2]


# print sum35c(20)


def sum35d(num):
    """Sum the arithmetic progressions: sum3 + sum5 - sum15

    Explicit version of the above

    for num = 20,
    3, 6, 9, 12, 15, 18 -> 6 terms
    5, 10, 15 -> 3 terms

    formulae:
    n * (a1 + an) / 2
    """
    # sum3 :
    a1 = 3
    n = (num - 1) // 3
    an = 3 * n
    sum3 = n * (a1 + an) / 2

    # sum 5:
    a1 = 5
    n = (num - 1) // 5
    an = 5 * n
    sum5 = n * (a1 + an) / 2

    # sum 15:
    a1 = 15
    n = (num - 1) // 15
    an = 15 * n
    sum15 = n * (a1 + an) / 2

    return sum3 + sum5 - sum15

print sum35d(20)





