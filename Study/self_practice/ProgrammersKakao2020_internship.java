package selftest;

import java.util.*;
public class ProgrammersKakao2020_internship {
	 public int[] solution(String[] gems) {
	        Set<String> set = new HashSet<String>();
	        
	        for(int i = 0; i<gems.length; i++){
	            set.add(gems[i]);   //중복 없이 보석 담기
	        }
	        
	        int start = 0;  //시작점 - 결과용
	        int temp = 0;   //시작점 - 임시용
	        int end = gems.length;   //끝점
	        
	        Map<String, Integer> map = new HashMap<>();  //key가 보석, value가 개수
	        Queue<String> q = new LinkedList<>();
	        
	        for(int i = 0; i<gems.length; i++){
	           if(map.containsKey(gems[i])) {
	                map.put(gems[i], map.get(gems[i]) + 1);
	            } 
	            else {
	                 map.put(gems[i], 1);
	            } //중복없이 보석이 map에 포함되면 value값 +1, 아니면 그대로 1
	            q.add(gems[i]);
	            
	            while(true){
	                String gem = q.peek(); //gem이 보석
	                if(map.get(gem) > 1){    //보석이 1개보다 더 들어옴(중복)
	                    q.poll(); //중복은 빼줘
	                    map.put(gem, map.get(gem) -1);   //보석 개수 -1
	                    temp++;
	                }
	                else{
	                    break;
	                }
	            }
	           
	            
	            if(set.size() == map.size()){
	                if(end > q.size()){
	                    end = q.size();
	                    start = temp;
	                }
	            }
	        }  
	            int[] answer = new int[2];
	            answer[0] = start + 1;
	            answer[1] = start + end;
	        
	            return answer;
	            
	        }
	}
   