package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_2609 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int num1 = Integer.parseInt(st.nextToken());
		int num2 = Integer.parseInt(st.nextToken());
		
		int gcd = GCD(num1, num2);
		int mcm = MCM(num1, num2);
		System.out.println(gcd);
		System.out.println(mcm);
	}
	
	public static int GCD(int num1, int num2) {
		
		if(num2 == 0) {
			return num1;
		}
		//G(a,b) = G(b,r) : r = (num1)mod(num2)
		return GCD(num2, (num1) % (num2));
	}
	
	public static int MCM(int num1, int num2) {
		return (num1 * num2) / GCD(num1, num2);
	}
}
