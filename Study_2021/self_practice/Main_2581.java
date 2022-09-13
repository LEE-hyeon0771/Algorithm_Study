package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main_2581 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int M = Integer.parseInt(br.readLine());
		int N = Integer.parseInt(br.readLine());
		int sum = 0;
		int min = 0;
		List<Integer> list = new ArrayList<>();
		
		for(int i = M; i<=N; i++) {
			boolean prime = true;
			if(i == 1) {
				continue;
			}
			for(int j = 2; j<=Math.sqrt(i); j++) {
				if(i%j == 0) {
					prime = false;                 //소수가 아니다
				}
			}
			if(prime) {                     //소수이면
				sum += i;                   //합
				list.add(i);                //리스트에 소수 다 담기
				min = list.get(0);          //리스트 맨 앞자리는 담은 소수 중 최솟값
			}
		}
		
		if(sum == 0) {                      //소수가 없을 때 -1
			System.out.println(-1);
		}
		else {                              //소수가 있을 때 합, 최솟값 출력
			System.out.println(sum);
			System.out.println(min);
		}
	}
}
