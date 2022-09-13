package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main_2292 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		int count = 1;
		int beeroom = 2;
		if(N==1) {
			count = 1;
		}
		else {
			while(beeroom < N) {
				beeroom += (count * 6);
				count++;
			}
		}	
		System.out.println(count);
	}
}
