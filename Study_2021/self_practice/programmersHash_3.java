package selftest;
import java.util.*;

public class programmersHash_3 {
	    public int solution(String[][] clothes) {
	        
	        Map<String, Integer> map = new HashMap<String, Integer>();
	        
	        for(int i = 0; i<clothes.length; i++){
	            map.put(clothes[i][1], map.getOrDefault(clothes[i][1],0) + 1);
	        }
	        
	        Iterator<String> ir = map.keySet().iterator();
	         int answer = 1;
	        while(ir.hasNext()){
	            String key = ir.next();
	            answer = answer * (map.get(key) + 1);
	        }
	        return answer-1;
	    }
	}

