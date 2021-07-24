import java.util.*;

class Program {
  public static boolean isValidSubsequence(List<Integer> array, List<Integer> sequence) {
    /* Keep a pointer in the sequence array if element
		found in the original array move the pointer.
		if the pointer goes till the last index print true else
		false */
		
		int seq_pointer = 0;
		
		for(int i = 0; i < array.size(); i++){
			if(seq_pointer < sequence.size() && array.get(i) == sequence.get(seq_pointer)){
				seq_pointer++;
			}
		}
		if(seq_pointer == sequence.size()){
			return true;
		}else{
    	return false;
  }
}
}
