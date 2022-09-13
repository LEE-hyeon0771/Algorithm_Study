package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_2846 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int arr[] = new int[N];
		
		for(int i = 0; i<N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		int temp = 0;
		int result = 0;
		for(int j = 0; j<N-1; j++) {
			if(arr[j] < arr[j+1]) {
				temp += arr[j+1]-arr[j];
			}
			else {
				temp = 0;
			}
			result = Math.max(temp, result);
		}
		System.out.println(result);
	}
}
