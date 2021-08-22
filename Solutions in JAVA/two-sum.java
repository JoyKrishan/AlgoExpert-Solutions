import java.util.*;

class Program {
  public static int[] twoNumberSum(int[] array, int targetSum) {
		HashSet<Integer> uniqueNums = new HashSet<Integer>();
		for (int i= 0; i < array.length; i++){
			int requiredNum = targetSum - array[i];
			if (uniqueNums.contains(requiredNum)){
				return new int[] {array[i], requiredNum};
			}
			if (!uniqueNums.contains(array[i])){
					uniqueNums.add(array[i]);
			}
		}
		
		return new int[0];
		}
	}
