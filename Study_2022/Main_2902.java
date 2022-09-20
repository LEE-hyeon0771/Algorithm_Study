package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_2902 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(),"-");      // "-" 단위로 단어 쪼개기
		
		StringBuilder sb = new StringBuilder();
		while(st.hasMoreTokens()) {          //"-" 로 끊어진 토큰(단어) 중 순회하면서 다음 토큰(단어) 찾기
			String input = st.nextToken();
			sb.append(input.charAt(0));      //단어 중 제일 처음 문자를 append
		}
		System.out.print(sb);
		
	}

}
