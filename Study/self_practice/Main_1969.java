package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_1969 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		String arr[] = new String[N];
		int DNAarr[][] = new int[M][26];
		
		for(int i = 0; i<N; i++) {
			arr[i] = br.readLine();
			for(int j = 0; j<M; j++) {
				int k = arr[i].charAt(j) - 'A';
				DNAarr[j][k]++;
			}
		}
		StringBuilder sb = new StringBuilder();
		for(int i = 0; i<M; i++) {
			int max = -1;
			int index = 0;
			for(int j = 0; j<26; j++) {
				if(DNAarr[i][j] > max) {
					max = DNAarr[i][j];
					index = j;
				}
			}
			sb.append((char)(index + 'A'));
		}
		System.out.println(sb.toString());
		
		int distance = 0;
		for(int i = 0; i<N; i++) {
			for(int j = 0; j<M; j++) {
				if(arr[i].charAt(j) != sb.charAt(j))
					distance++;
			}
		}
		System.out.println(distance);
	}

}
