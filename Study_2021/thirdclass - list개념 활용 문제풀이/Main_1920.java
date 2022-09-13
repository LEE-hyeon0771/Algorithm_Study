package thirdclass;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main_1920 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		
		int array[] = new int[n];
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		for(int i = 0; i<n; i++) {
			array[i]=Integer.parseInt(st.nextToken());
		}
		Arrays.sort(array);
		
		int m = Integer.parseInt(br.readLine());
		
		st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		for(int j = 0; j<m; j++) {
			int num = Integer.parseInt(st.nextToken());
			
			int start=0, stop=n-1;
			while(start<=stop) {
				
				int midnum = (start+stop)/2;
				
				if(array[midnum] > num) {
					stop = midnum - 1;
				}
				else if(array[midnum] < num){
					start = midnum + 1;
				}
				else {
					//System.out.println("1");
					sb.append(1+"\n");
					break;
				}
			}
			if(start > stop) {
				//System.out.println("0");
				sb.append(0+"\n");
			}
			
		}
		System.out.println(sb.toString());
	}

}
