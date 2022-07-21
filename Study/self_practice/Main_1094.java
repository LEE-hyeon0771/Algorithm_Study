package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main_1094 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int X = Integer.parseInt(br.readLine());
		
		int bar = 64;
		int count = 0;
		while(X>0) {
			if(X == 64) {
				count++;
				break;
			}
			if(X<bar) {
				bar = bar / 2;
			}
			else {
				X = X - bar;
				count++;
			}
		}
		System.out.println(count);
	}
}
