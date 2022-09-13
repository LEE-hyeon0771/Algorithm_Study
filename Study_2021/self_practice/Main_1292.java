package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main_1292 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int A = Integer.parseInt(st.nextToken());
		int B = Integer.parseInt(st.nextToken());
		
		List<Integer> list = new ArrayList<>();
		
		for(int i = 1; i<=1000; i++) {
			for(int j = 0; j<i; j++) {
				list.add(i);
			}
		}
		
		int sum = 0;
		for(int i = A-1; i<=B-1; i++) {
			sum += list.get(i);
		}
		System.out.println(sum);
	}

}
