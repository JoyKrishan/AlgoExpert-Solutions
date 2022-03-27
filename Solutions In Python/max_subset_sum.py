def max_subset_sum(array):
    # maxSum[i] = max(maxSum[i-1], maxSum[i-2]+array[i])
    
    # edge case when empty array 
    if len(array) == 0:
        return 0
    elif len(array) == 1:
        return array[0]
    maxSums = array[:]
    maxSums[1] = max(maxSums[0], maxSums[1])

    for i in range(2, len(array)):
        maxSums[i] = max(maxSums[i-1], maxSums[i-2]+array[i])
    
    return maxSums[-1]
