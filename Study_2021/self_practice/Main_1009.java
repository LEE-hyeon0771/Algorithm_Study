package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_1009 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		
		StringBuilder sb = new StringBuilder();
		for(int i = 0; i<T; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int result = 1;
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			
			if(result % 10 > 0) {
				for(int j = 0; j<b; j++) {
					result = result * a % 10;
					
				}
			}
			if(result%10 == 0) {
				result = 10;
				
			}
			sb.append(result + "\n");
			
		}
		System.out.println(sb.toString());
	}

}
