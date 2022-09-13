package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_4344 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int C = Integer.parseInt(br.readLine());
		
		for(int i = 0; i<C; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int[] arr = new int[N];
			
			double sum = 0;
			for(int j = 0; j<N; j++) {
				arr[j]= Integer.parseInt(st.nextToken());
				sum += arr[j];
			}
			
			double avg = sum/N;
			
			double count = 0;
			for(int j = 0; j<N; j++) {
				if(arr[j] > avg) {
					count++;
				}
			}
			double percent = (count/N) * 100;
			System.out.printf("%.3f%%\n",percent);
		}	
	}
}
