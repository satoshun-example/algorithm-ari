#!/usr/local/bin/python3

##くじ引き##

def kujibiki1(n: int, m: int, k: list):
    size = len(k)
    for x1 in range(size):
        for x2 in range(size):
            for x3 in range(size):
                for x4 in range(size):
                    if k[x1] + k[x2] + k[x3] + k[x4] == m:
                        return True
    return False


if __name__ == '__main__':
    for (n, m, k, result) in [
        (3, 10, [1, 3, 5], True),
        (3, 9, [1, 3, 5], False)
    ]:
        assert result == kujibiki1(n, m, k)

    print("success!!")
