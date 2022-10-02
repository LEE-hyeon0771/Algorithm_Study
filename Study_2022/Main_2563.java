package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_2563 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	    
		int N = Integer.parseInt(br.readLine());
		boolean arr[][] = new boolean[100][100];
		
		int count = 0;
		//StringTokenizer st;
		for(int i = 0; i<N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int k = Integer.parseInt(st.nextToken());
			int t = Integer.parseInt(st.nextToken());
			
			for(int j = k; j<k+10; j++) {
				for(int p = t; p<t+10; p++) {
					if(arr[j][p] == false) {
					arr[j][p] = true;
					count++;
					}
				}
			}
		}
		System.out.println(count);
	}
}
