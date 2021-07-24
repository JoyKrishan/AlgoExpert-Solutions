def isValidSubsequence(array, sequence):
	rev_sequence = sequence.copy()
	rev_sequence.reverse()
	for elem in array:
		if not rev_sequence:
			break
		if elem == rev_sequence[-1]:
			rev_sequence.pop()
	
	if not rev_sequence:
		return True
	else:
		return False
			
		
