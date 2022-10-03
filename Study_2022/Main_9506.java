package selftest;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main_9506 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		while(true) {
			int n = Integer.parseInt(br.readLine());
			
			StringBuilder sb = new StringBuilder();
			int sum = 0;
			for(int i = 1; i<n; i++) {
				if(n % i == 0) {
					sb.append(i + " + ");
					sum += i;
				}
			}
			if(sum != n) {
				System.out.println(n + " is Not perfect.");
				continue;
			}
			else {
				System.out.println(n + " = " + sb.toString().substring(0, sb.length()-3));
			}
			if(n == -1) {
				break;
			}
		}
	}
}