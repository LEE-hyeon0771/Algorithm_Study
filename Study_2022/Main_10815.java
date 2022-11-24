package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main_10815 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringBuilder sb = new StringBuilder();
		
		int N = Integer.parseInt(br.readLine());
		int arr[] = new int[N];
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		for(int i = 0; i<N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		Arrays.sort(arr);
		int M = Integer.parseInt(br.readLine());
		
		st = new StringTokenizer(br.readLine());
		for(int i = 0; i<M; i++) {
			int num = Integer.parseInt(st.nextToken());
			sb.append(binarySearch(arr, N, num) + " ");
		}
		System.out.println(sb.toString());
		
	}
	
	public static int binarySearch(int[] arr, int n, int target) {
		int low = 0;
		int high = n-1;
		int mid = 0;
		
		while(low <= high) {
			mid = (low + high) / 2;
			
			if(arr[mid] == target) {
				return 1;
			}
			
			if(arr[mid] < target) {
				low = mid + 1;
			}
			else {
				high = mid - 1;
			}
		}
		return 0;
	}
}
