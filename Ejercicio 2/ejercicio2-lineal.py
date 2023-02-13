def common_substring(s1, s2, s3):
    result = ""
    for i in range(len(s1)):
        for j in range(i + 1, len(s1) + 1):
            s = s1[i:j]
            if s in s2 and s in s3:
                if len(s) > len(result):
                    result = s
    return result

m, n, k = [int(x) for x in input().split()]
s1 = input()
s2 = input()
s3 = input()
print(common_substring(s1, s2, s3))