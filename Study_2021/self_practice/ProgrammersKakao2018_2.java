package selftest;

public class ProgrammersKakao2018_2 {
	    public String[] solution(int n, int[] arr1, int[] arr2) {
	        String[] answer = new String[n];
	       
	        for(int i = 0; i<answer.length; i++){
	            String s = Integer.toBinaryString(arr1[i] | arr2[i]);
	            
	            if(s.length() < n){
	                for(int j = s.length(); j < n; j++){
	                    s = 0 + s;
	                }
	                
	            }
	            
	            s = s.replace("1","#");
	            s = s.replace("0"," ");
	            
	            answer[i] = s;
	        }
	        return answer;
	    }
	}

