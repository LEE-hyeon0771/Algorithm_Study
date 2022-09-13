package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main_2635 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		List<Integer> max = new ArrayList<>();     //max 숫자 출력용
		int maxnum = 0;                            //maxnum 8 출력용
		for(int i = 1; i<=N; i++) {
			List<Integer> now = new ArrayList<>();        //실제 처리 리스트
			now.add(N);
			now.add(i);
			int first = N;
			int second = i;
			
			while(true) {                             //이전 수 교체해가면서 앞-뒤 숫자 만들기
				int result = first - second;
				if(result >= 0) {
					now.add(result);
				}
				else {
					break;
				}
				
				first = second;
				second = result;
			}
			
			if(max.size() <= now.size()) {              //최대수가 실제 처리 리스트 크기보다 더 작게 되 경우
				maxnum = now.size();               //최대수가 실제 처리 리스트 크기가 되고 그냥 최대 list도 실제 처리 list인 now가 된다.
				max = now;
			}
		}
		System.out.println(maxnum);
		for(int i = 0; i<max.size(); i++) {
			System.out.print(max.get(i) + " ");
		}
	}
}
