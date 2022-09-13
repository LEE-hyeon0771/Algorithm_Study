package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main_1110 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		int count = 0;
		int result = N;
		while(true) {
			N = (N%10)*10 + ((N/10) + (N%10))%10;
			count++;
			
			if(result == N) {
				break;
			}
		}
		
		System.out.println(count);
	}

}
