package selftest;
import java.util.*;
public class ProgrammersTest3 {
	    public int[] solution(int[] array, int[][] commands) {
	        int[] answer = {};
	        answer = new int[commands.length];
	        List<Integer> list = new ArrayList<Integer>();  
	        
	        for(int i = 0; i<commands.length; i++){
	            list.clear();
	            int start = commands[i][0];
	            int stop = commands[i][1];
	            
	            for(int j = start; j<=stop; j++){
	                list.add(array[j-1]);
	            }
	            Collections.sort(list);
	            answer[i] = list.get(commands[i][2]-1);
	        }
	        
	        
	        return answer;
	    }
	}

