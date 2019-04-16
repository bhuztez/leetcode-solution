def minDistance(word1, word2):
    l1 = len(word1)
    l2 = len(word2)

    m = [[0 for _ in range(l1+1)] for _ in range(l2+1)]

    for i in range(l1+1):
        m[0][i] = i

    for i in range(l2+1):
        m[i][0] = i

    for i in range(1, l2+1):
        for j in range(1, l1+1):
            d1 = m[i-1][j] + 1
            d2 = m[i][j-1] + 1
            d3 = m[i-1][j-1] + (1 if word1[j-1] != word2[i-1] else 0)

            m[i][j] = min(d1, d2, d3)

    return m[-1][-1]
