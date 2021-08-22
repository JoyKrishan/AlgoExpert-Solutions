def twoNumberSum(array, targetSum):
    unique_numbers = set()
    for num in array:
        if num not in unique_numbers:
            unique_numbers.add(num)
            required_num = targetSum - num
        if required_num == num:
            continue
        elif required_num in unique_numbers:
            return [num, required_num]
    
    return []
		
