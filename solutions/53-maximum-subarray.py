def maxSubArray(A):
    current_sum, max_sum = A[0], A[0]
    for n in A[1:]:
        current_sum = max(current_sum+n, n)
        max_sum = max(current_sum, max_sum)
    return max_sum
