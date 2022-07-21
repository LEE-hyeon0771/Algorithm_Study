package selftest;

public class ProgrammersKakao2019_level1 {
	    public int[] solution(int N, int[] stages) {
	        double[] failrates = new double[N];   //실패율
	        
	        for(int i = 1; i<=N; i++){
	            double nonpasser = 0;    //도달만 개수세는 변수
	            double passer = 0;       //넘어가서 패스 개수세는 변수
	            
	            for(int j = 0; j<stages.length; j++){
	                if(i == stages[j]){        //도달만 변수 카운트
	                    nonpasser++;
	                }
	                if(i <= stages[j]){        //넘어간 패스 변수 카운트
	                    passer++;
	                }
	            }
	            
	            if(nonpasser == 0){         //스테이지 도달만 한 사람도 없으면
	                failrates[i-1] = 0;     //실패율 0
	                continue;
	            }
	            failrates[i-1] = nonpasser/passer;   //실패율 정의
	        }
	        
	        int[] result = new int[N];       
	        
	        for(int i = 0; i<failrates.length; i++){
	            double max = -1;
	            int index = 0;
	            
	            for(int j = 0; j<failrates.length; j++){    //실패율 max값 찾기
	                if(max < failrates[j]){
	                    max = failrates[j];
	                    index = j;          //max 인덱스를 index로 해줌
	                }
	            }
	            failrates[index] = -1;       //계속 반복해서 for문 안에서 찾을 수 있도록 -1로 다시 셋팅  
	            result[i] = index+1;
	        }
	        return result;
	    }
	}

