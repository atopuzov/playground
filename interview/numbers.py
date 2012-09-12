def factorial(n):
    if n < 0:
        raise("Not defined for negative numbers")

    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def factorial_i(n):
    if n < 0:
        raise("Not defined for negative numbers")
    m = 1
    for i in xrange(1,n+1):
        m *= i

    return m        

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_i(n):
    n_m1 = 1
    n_m2 = 1

    if n == 0 or n == 1:
        return 1
    else:
        for i in xrange(2,n+1):
            sum = n_m1+n_m2
            n_m2 = n_m1
            n_m1 = sum

        return sum

def fib_l(n):
    fibs = [1,1]
    for i in range(2, n+1):
        fibs.append(fibs[i-1] + fibs[i-2])
    return fibs[n]

print factorial(2), factorial(3), factorial(4), factorial(5)
print factorial_i(2), factorial_i(3), factorial_i(4), factorial_i(5)
print fib(0), fib(1), fib(2), fib(3), fib(4), fib(5)
print fib_i(0), fib_i(1), fib(2), fib_i(3), fib_i(4), fib_i(5)
print fib_l(0), fib_l(1), fib(2), fib_l(3), fib_l(4), fib_l(5)
