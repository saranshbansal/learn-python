# Count number of 1s in decimal representation of 11^N


def solution(num, N):
    if N == 0:
        return 1

    return count_digits(num**N, "1")


def count_digits(num, digit):
    print(num)
    count = 0

    for ch in str(num):
        if ch == digit:
            count += 1

    return count


print(solution(11, 2))
