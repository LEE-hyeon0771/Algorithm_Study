package selftest;
import java.util.*;
public class Programmers_number_plus {
	
	public int[] solution(int[] numbers) {
	        
	    	Set<Integer> set = new HashSet<Integer>();
	        
	        for(int i = 0; i<numbers.length; i++){
	            for(int j = i+1; j<numbers.length; j++){
	                int result = numbers[i] + numbers[j];
	                set.add(result);
	            }
	        }
	        
	        int[] answer = new int[set.size()];
	        
	        Iterator<Integer> ir = set.iterator();
	        int index = 0;
	        while(ir.hasNext()){
	            answer[index++] = ir.next(); 
	        }
	        Arrays.sort(answer);
	        return answer;    
	}    
}
