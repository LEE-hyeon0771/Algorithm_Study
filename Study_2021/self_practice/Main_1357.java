package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_1357 {
	public static int Rev(int a) {
		String str = "";
		while(a>0){
			str += a%10;
			a = a/10;
		}
		return Integer.parseInt(str);
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int x = Integer.parseInt(st.nextToken());
		int y = Integer.parseInt(st.nextToken());
		
		int result = Rev(Rev(x) + Rev(y));
		
		System.out.println(result);
	}

	
}