package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Main_2161 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		Queue<Integer> q = new LinkedList<Integer>();
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		for(int i = 1; i<=N; i++) {
			q.add(i);
		}
		StringBuilder sb = new StringBuilder();
		while(!q.isEmpty()) {
			sb.append(q.poll() + " ");
			if(q.isEmpty()) {
				break;
			}
			q.add(q.poll());
		}
		System.out.println(sb.toString());
	}

}
