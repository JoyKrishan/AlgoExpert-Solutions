def kadaneAlgorithm(array):
    if len(array) == 0:
        return 
    if len(array) == 1:
        return array[0]
    maxSumEndingHere = array[:]

    for i in range(1, len(array)):
        maxSumEndingHere[i] = max(maxSumEndingHere[i-1] + array[i], array[i])
    return max(maxSumEndingHere)