package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main_1789 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		long S = Long.parseLong(br.readLine());
		long sum = 0;
		int count = 0;
		
		while(true) {
			sum += count;
			if(sum > S) {
				break;
			}
			count++;
		}
		int N = count-1;
		System.out.println(N);
	}
}
