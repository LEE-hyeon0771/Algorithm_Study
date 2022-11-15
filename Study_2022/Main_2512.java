package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main_2512 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int low = 0;
		int high = -1;
		int N = Integer.parseInt(br.readLine());
		
		int arr[] = new int[N];
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		
		for(int i = 0; i<N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
			high = Math.max(high, arr[i]);
		}
		int M = Integer.parseInt(br.readLine());
		
		//Arrays.sort(arr);
		
		while(low <= high){
			long sum = 0;
			int mid = (low + high) / 2;
			
			for(int i = 0; i<N; i++) {
				if(arr[i] > mid) {
					sum += mid;
				}
				else {
					sum += arr[i];
				}
			}
			if(sum <= M) {
				low = mid + 1;
			}
			else {
				high = mid - 1;
			}
		}
		System.out.println(high);
	}
}
