package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main_2231 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		for(int i = 1; i<N; i++) {       //생성자를 N안쪽에서 계속 체크
			int num = i;  //생성자 숫자 변수
			int sum = i;   //분해합 변수 sum에 생성자 값 i를 넣고 합 시작
			while(num != 0) {
				sum = sum + (num % 10);  //198 % 10 = 8, 19 % 10 = 9, 1 % 10 = 1   (198 + 8 + 9 + 1)
				num = num/10;         //198 / 10 = 19, 19 / 10 = 1 
			}
			
			if(sum == N) {      //찾은 생성자의 분해합이 입력 받은 수와 일치하면 결과 변수에 넣고 반복문 종료 -> 최소 생성자
				System.out.println(i);
				return;
			}
		}
		System.out.println(0);
	}
}
