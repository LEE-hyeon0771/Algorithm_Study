package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main_1075 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		int F = Integer.parseInt(br.readLine());
		
		N = (N/100) * 100;         //N의 뒷자리수 두개를 00으로 변환
		StringBuilder sb = new StringBuilder();
		while(true) {
			if(N % F == 0) {
				int result = N % 100;           //N이 F로 나누어 떨어질 때 N을 100으로 나눈 나머지 값을 result로 만듦 - 뒤 두자리 수 표현
				if(result < 10) {
					sb.append("0" + result);         //result가 10보다 작으면 02 이런식으로 표현하기 위해서 앞에 0붙여줌
				}
				else {
					sb.append(result);
				}
				System.out.println(sb.toString());
				break;
			}
			N++;
		}
	}
}
