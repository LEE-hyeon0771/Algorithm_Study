package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_15953 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int N = Integer.parseInt(br.readLine());
		
		for(int i = 0; i<N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int num1 = Integer.parseInt(st.nextToken());
			int num2 = Integer.parseInt(st.nextToken());
			
			sb.append(FirstFes(num1) + SecondFes(num2)).append('\n');
		}
		
		System.out.println(sb.toString());

	}
	
	public static int FirstFes(int n) {
		if(n == 1) {
			return 5000000;
		}
		else if(1<n && n<=3) {
			return 3000000;
		}
		else if(3<n && n<=6) {
			return 2000000;
		}
		else if(6<n && n<=10) {
			return 500000;
		}
		else if(10<n && n<=15) {
			return 300000;
		}
		else if(15<n && n<=21) {
			return 100000;
		}
		else
			return 0;
	}
	
	public static int SecondFes(int n) {
		if(n == 1) {
			return 5120000;
		}
		else if(1<n && n<=3) {
			return 2560000;
		}
		else if(3<n && n<=7) {
			return 1280000;
		}
		else if(7<n && n<=15) {
			return 640000;
		}
		else if(15<n && n<=31) {
			return 320000;
		}
		else 
			return 0;
	}
}

