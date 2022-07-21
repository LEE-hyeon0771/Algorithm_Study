package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_1712 {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		int[] array = new int[3];
		for(int i = 0; i<3; i++) {
			array[i] = Integer.parseInt(st.nextToken());
		}
		int a = array[0];
		int b = array[1];
		int c = array[2];
		
		if(c>b) {
			int n = (a/(c-b)) + 1;
			System.out.println(n);
		}
		else {
			System.out.println(-1);
		}
	}

}
