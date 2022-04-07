def longestPalindromeSubstring(string):
    currentLongest = [0, 1]
    for i in range(1, len(string)):
        # aba -> where we start from b 
        odd = getLongestPalindromeFrom(string, i-1, i+1 ) # string, left, right
        # abba -> where we start in between both b's
        even = getLongestPalindromeFrom(string, i-1, i)
        longest = max(even, odd, key= lambda x: x[1] - x[0])
        currentLongest = max(currentLongest, longest, key = lambda x: x[1] - x[0])
    
    return string[currentLongest[0]:currentLongest[1]]

def getLongestPalindromeFrom(string, leftIdx, rightIdx):
    while leftIdx >= 0 and rightIdx < len(string):
        if string[leftIdx] != string[rightIdx]:
            break
        leftIdx -= 1
        rightIdx += 1
    
    return [leftIdx + 1, rightIdx]
