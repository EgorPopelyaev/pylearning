def reverse(s):
    length = len(s)

    if length < 2:
        return s

    rev_str = ""
    i = 0

    while i < length:
        rev_str = rev_str + reverse(s[(length - 1) - i])
        i += 1

    return rev_str


def permute(s):
    out = []

    # Base Case
    if len(s) == 1:
        out = [s]

    else:
        # For every letter in string
        for i, let in enumerate(s):

            # For every permutation resulting from Step 2 and 3 described above
            for perm in permute(s[:i] + s[i + 1:]):
                # Add it to output
                out += [let + perm]

    return out


def fib_rec(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)


print "Fib_rec: %d" % fib_rec(10)


def fib_iter(n):
    a = 0
    b = 1

    for i in range(n):
        a, b = b, a + b

    return a


print "Fib iter: %r" % fib_iter(10)

n = 10
cache = [None] * (n + 1)


def fib_dyn(n):
    if n == 0 or n == 1:
        return n

    if cache[n] != None:
        return cache[n]

    cache[n] = fib_dyn(n - 1) + fib_dyn(n - 2)

    return cache[n]


print "Fib dyn: %r" % fib_dyn(n)
