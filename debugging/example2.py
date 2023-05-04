# a particularly contrived example to demonstrate stepping and breakpoints


def long_func(n):
    # doesn't really do anything, just a long function
    x = 1
    y = 2
    z = x * y
    z = z**2
    yp = y + 1 if y > 0 else y - 1
    zz = z + yp
    q = max(zz, yp)
    lb = q - 1 & 0x0F
    hb = q >> 4
    q = lb + hb
    c = yp / (lb + q)
    return q


def bad_approx_sqrt(n):
    # don't actually do this

    not_needed = long_func(n)
    for upper in range(2, n):
        if upper * upper > n:
            break

    lower = upper - 1
    iterations = 1000

    for x in range(iterations):
        guess = lower + x / iterations
        if guess * guess > n:
            return guess - 1 / iterations


def main():
    x = 65
    for x in range(60, 82):
        s = bad_approx_sqrt(x)
        print(f"The square root of {x} is approximately {s:.2f}")


if __name__ == "__main__":
    main()
