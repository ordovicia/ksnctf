import math

PI_STR = "31415926535897"
PI_STR_LEN = len(PI_STR)


def is_prime(x):
    ceil = math.ceil(math.sqrt(x))
    for i in range(2, ceil):
        if x % i == 0:
            return False
    return True


def main():
    DIGITS_LEN = 10

    for i in range(0, PI_STR_LEN - DIGITS_LEN + 1):
        digits = PI_STR[i:(i + DIGITS_LEN)]
        if digits[0] == '0':
            continue

        digits = int(digits)
        if is_prime(digits):
            print(digits)
            break


if __name__ == '__main__':
    main()
