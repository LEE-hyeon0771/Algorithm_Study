package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_11050 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		
		int result = Factorial(N) / (Factorial(K) * Factorial(N-K));
		
		System.out.println(result);
	}
	
	public static int Factorial(int n) {
		if(n==0 || n==1) {
			return 1;
		}
		else {
			return n * Factorial(n-1);
		}
	}
	
}

