str1 = "Hi"
str2 = "HEllo"


def dist(a, b):
    def rec(i, j):
        if i == 0 or j == 0:
            return max(i, j)
        elif a[i-1] == b[j-1]:
            return rec(i-1, j-1)
        else:
            return 1 +min(
                rec(i, j-1),
                rec(i-1, j),
                rec(i-1, j-1),
            )
    return rec(len(a), len(b))

lev = dist(str1, str2)
bigger = max[(len(str1), len(str2))]
pct = ((bigger - lev) / bigger) * 100
print(pct)