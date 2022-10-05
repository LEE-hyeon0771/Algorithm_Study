package selftest;

import java.util.Scanner;

public class Main14659 {

	public static void main(String[] args){
		
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int arr[] = new int[N];
		
		int max = 0;
		for(int i = 0; i<N; i++) {
			
			arr[i] = sc.nextInt();
		}
		for(int i = 0; i<N; i++) {
			int kill = 0;
			for(int j = i+1; j<N; j++) {
				if(arr[i] > arr[j]) {
					kill++;
				}
				else {
					break;
				}
			}
			max = Math.max(max, kill);
		}
		System.out.println(max);
	}
}
