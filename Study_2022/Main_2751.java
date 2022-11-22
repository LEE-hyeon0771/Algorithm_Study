package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main_2751 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		List<Integer> list = new ArrayList<Integer>();
		
		for(int i = 0; i<N; i++) {
			int num = Integer.parseInt(br.readLine());
			list.add(num);
			
		}
		
		Collections.sort(list);
		StringBuilder sb = new StringBuilder();
		for(int i = 0; i<list.size(); i++) {
			sb.append(list.get(i)).append('\n');
		}
		System.out.println(sb.toString());
	}
}
