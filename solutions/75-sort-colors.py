def sortColors(A):
    count = [0,0,0]
    for i in A:
        count[i] += 1

    i = 0

    for j in [0,1,2]:
        while count[j]:
            A[i] = j
            count[j] -= 1
            i += 1
