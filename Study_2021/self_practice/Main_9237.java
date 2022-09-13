package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main_9237 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		Integer arr[] = new Integer[N];
		
		for(int i = 0; i<N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		Arrays.sort(arr, Collections.reverseOrder());
		
		int max = 0;
			
		for(int i = 0; i<N; i++) {
			arr[i] = arr[i]+i+1;  //나무 자라는 일수 + 심는데 걸린 일수 1일
			max = Math.max(max, arr[i]);
		}
		System.out.println(max+1);  //사는데 1일
	}
}
