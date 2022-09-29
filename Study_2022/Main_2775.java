package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main_2775 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		int arr[][] = new int[15][15];
		
		for(int i = 0; i<15; i++) {
			arr[i][1] = 1;
			arr[0][i] = i;
		}
		
		for(int k = 1; k<15; k++) {
			for(int n = 1; n<15; n++) {
				arr[k][n] = arr[k][n-1] + arr[k-1][n];
			}
		}
		StringBuilder sb = new StringBuilder();
		for(int i = 0; i<T; i++) {
			int k = Integer.parseInt(br.readLine());
			int n = Integer.parseInt(br.readLine());
		
			sb.append(arr[k][n] + "\n");
		}
		System.out.println(sb.toString());
	}
}
