""" Report number of numbers consisting of N digits, that have value > 0 and
 are divisible by M.
 She gives you X pairs of numbers, each pair consists of 2 numbers from 1 to 9.
 Given these pairs , assume one of them to be consisting of numbers a and b,
 eliminate out all numbers in which a and b appear adjacent to each other
"""
MOD = 10**9 + 7


def f(i, mod, lastDig):
    # i is the current length, current mod, last inserted digit
    # okay: no case of adjacency
    ans = dp[i][mod][lastDig]
    if ans != -1:
        return ans
    ans = 0
    if i == N:
        ans = 1 if mod == 0 else 0

    # else we can choose any of the digits
    # caveat: init digit can not be 0
    else:
        for dig in xrange(10):
            if i == 0 and dig == 0:
                continue
            elif i == 0:
                ans = (ans + f(i + 1, dig % M, dig)) % MOD

            # else check if to be inserted digit
            elif _PAIR[lastDig][dig] == 0:
                ans = (ans + f(i + 1, (mod * 10 + dig) % M, dig)) % MOD

    dp[i][mod][lastDig] = ans % MOD
    return ans

if __name__ == '__main__':
    # Precompute modular matrix

    for _ in xrange(input()):
        # Prepare digit matrix
        _PAIR = [[0] * 10 for i in xrange(10)]

        N, M, X = map(int, raw_input().split())
        for __ in xrange(X):
            a, b = map(int, raw_input().split())
            _PAIR[a][b] = _PAIR[b][a] = 1

        dp = [[[-1 for i in xrange(11)] for j in xrange(101)]
              for k in xrange(1001)]
        print f(0, 0, 0)
