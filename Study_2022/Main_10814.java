package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_10814 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		
		StringBuilder[] arr = new StringBuilder[201];
		
		for(int i = 0; i < arr.length; i++) {
			arr[i] = new StringBuilder();    //按眉 硅凯俊 StringBuilder 按眉 积己
		}
		
		for(int i = 0; i<N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int num = Integer.parseInt(st.nextToken());
			String name = st.nextToken();
			arr[num].append(num).append(' ').append(name + '\n');
			
		}
		StringBuilder sb = new StringBuilder();
		for(StringBuilder s : arr) {
			sb.append(s);
		}	
		System.out.println(sb);
	}
}
