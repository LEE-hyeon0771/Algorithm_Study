package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main_1436 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		int num = 0;
		int count = 0;
		while(true) {
			num++;
			String str = String.valueOf(num);
			if(str.contains("666")) {
				count++;
			}
			if(N == count) {
				break;
			}
		}
		System.out.println(num);
	}
}
