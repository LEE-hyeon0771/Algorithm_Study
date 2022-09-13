package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_1010 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int arr[][] = new int[30][30];
		
		for(int i = 0; i<30; i++) {
			arr[i][i] = 1;
			arr[i][0] = 1;
			arr[i][1] = i;
		}
		
		for(int i = 1; i<30; i++) {
			for(int j = 1; j<30; j++) {
				arr[i][j] = arr[i-1][j-1] + arr[i-1][j];
			}
		}
		
		int T = Integer.parseInt(br.readLine());
		
		StringBuilder sb = new StringBuilder();
		for(int i = 0; i<T; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			
			int N = Integer.parseInt(st.nextToken());
			int M = Integer.parseInt(st.nextToken());
			
			sb.append(arr[M][N] + "\n");
		}
		System.out.println(sb.toString());
	}
}
