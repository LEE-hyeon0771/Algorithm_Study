package selftest;

public class Programmers_dfs_targetNumber {
	    public static int answer = 0;
	        
	    public void dfs(int[] numbers, int target, int idx, int result){
	        if(idx == numbers.length){
	            if(result == target){
	                answer++;
	            }
	        }
	        else{
	            dfs(numbers, target, idx+1, result-numbers[idx]);
	            dfs(numbers, target, idx+1, result+numbers[idx]);
	            }
	        }
	    public int solution(int[] numbers, int target) {
	            
	            dfs(numbers, target, 1, -numbers[0]);
	            dfs(numbers, target, 1, numbers[0]);
	    
	        return answer;
	    }
	}

