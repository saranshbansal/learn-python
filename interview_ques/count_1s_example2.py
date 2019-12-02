# Count number of 1s in binary representation of A*B


def solution(A, B):
    if isinstance(A, int) and isinstance(B, int):
        bin_rep = bin(A * B)
        print(bin_rep)
        return bin_rep.count("1")
    return 0


print(solution(10, 5))

