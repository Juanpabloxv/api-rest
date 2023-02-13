def lcs(s1, s2, s3):
    n1 = len(s1)
    n2 = len(s2)
    n3 = len(s3)
    lcs = [[[0 for _ in range(n3 + 1)] for _ in range(n2 + 1)] for _ in range(n1 + 1)]
    result = ""
    len_result = 0

    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            for k in range(1, n3 + 1):
                if s1[i - 1] == s2[j - 1] == s3[k - 1]:
                    lcs[i][j][k] = lcs[i - 1][j - 1][k - 1] + 1
                    if lcs[i][j][k] > len_result:
                        len_result = lcs[i][j][k]
                        result = s1[i - len_result: i]
                else:
                    lcs[i][j][k] = 0

    return result


m, n, k = [int(x) for x in input().split()]
s1 = input().strip()
s2 = input().strip()
s3 = input().strip()

print(lcs(s1, s2, s3))