package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_1018 {
	public static boolean[][] arr;
	public static int answer = Integer.MAX_VALUE;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		arr = new boolean[N][M];
		
		for(int i = 0; i<N; i++) {
			String str = br.readLine();
			for(int j = 0; j<M; j++) {
				if(str.charAt(j) == 'W') {
					arr[i][j] = true;
				}
				else {
					arr[i][j] = false;
				}
			}
		}
		for(int i = 0; i<N-7; i++) {
			for(int j = 0; j<M-7; j++) {
				counting(i,j);
			}
		}
		System.out.println(answer);
	}
	
	public static void counting(int x, int y) {
		int count = 0;
		boolean check = arr[x][y];
		for(int i = x; i<x+8; i++) {
			for(int j = y; j<y+8; j++) {
				if(arr[i][j] != check) {          //올바른 색 X -> count++
					count++;
				}
				check = !check;
			}
			check = !check;
		}
		
		count = Math.min(count, 64 - count);
		answer = Math.min(answer, count);
	}
}
