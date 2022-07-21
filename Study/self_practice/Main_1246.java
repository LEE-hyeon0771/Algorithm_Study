package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class Main_1246 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		List<Integer> list = new ArrayList<>();      //Pi 담을 list
		
		for(int i = 0; i<M; i++) {
			list.add(Integer.parseInt(br.readLine()));
		}
		int max = 0;              //max 출력값
		int maxPi = 0;
		
		Collections.sort(list);      //list 정렬
		
		for(int i = 0; i<list.size(); i++) {
			int now = 0;
			int nowPi = list.get(i);      //현재 Pi에 list에 담긴 Pi 뽑아오기
			
			if(M - i < N) {               //앞으로 살 사람이 N보다 작은 경우는 M-i를, 그렇지않다면 N을 그대로 곱해줌 
				now = nowPi * (M-i);
			}
			else {
				now = nowPi * N;
			}
			
			if(max < now) {            //max값이 now값 보다 작을때 max에 now값을 maxPi에 nowPi 담기
				max = now;
				maxPi = nowPi;
			}
		}
		System.out.print(maxPi + " " + max);
	}
}
