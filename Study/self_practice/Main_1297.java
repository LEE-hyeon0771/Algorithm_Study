package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_1297 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int[] arr = new int[3];
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		for(int i = 0; i<3; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		double k;
		int d = arr[0];
		int h = arr[1];
		int w = arr[2];
		
		k = Math.sqrt(Math.pow(d, 2) / (Math.pow(h, 2) + Math.pow(w, 2)));
		
		System.out.print((int)Math.floor(h*k) + " ");
		System.out.println((int)Math.floor(w*k));
	}

}
