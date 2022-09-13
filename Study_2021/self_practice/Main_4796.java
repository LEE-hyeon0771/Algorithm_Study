package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_4796 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int count = 0;
		
		StringBuilder sb = new StringBuilder();
		while(true) {
			
			count++;
			
			StringTokenizer st = new StringTokenizer(br.readLine());
			
			int L = Integer.parseInt(st.nextToken());   //5
			int P = Integer.parseInt(st.nextToken());   //8
			int V = Integer.parseInt(st.nextToken());   //20
			
			if(L==0) {
				break;
			}
			
			int result = (V/P) * L + Math.min((V%P), L);
			
			sb.append("Case " + count + ": " + result + "\n");
			
		}
		System.out.println(sb.toString());
	}
}


