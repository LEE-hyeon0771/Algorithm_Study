package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main_11720 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		String num = br.readLine();
		int temp = 0;
		int sum = 0;
		for(int i = 0; i<N; i++) {
			temp = num.charAt(i) - '0';
			sum += temp;
		}
		System.out.println(sum);
	}
}
