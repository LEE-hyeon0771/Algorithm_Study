package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main_2810 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		String str = br.readLine();
		int count = 1;
		for(int i = 0; i<N; i++) {
			
			if(str.charAt(i) == 'S') {
				count++;
			}
			else if(str.charAt(i) == 'L') {
				i++;
				count++;
			}
		}
		
		if(N > count) {
			System.out.println(count);
		}
		else {
			System.out.println(N);
		}
	}
}
