def digit_sum(n):
    if n == 0:
        return 0

    return n % 10 + digit_sum(n // 10)


def main():
    n = int(input())
    print(digit_sum(abs(n)))


if __name__ == "__main__":
    main()