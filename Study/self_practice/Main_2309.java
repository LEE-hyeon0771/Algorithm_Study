package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main_2309 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int[] height = new int[9];
		
		int sum = 0;
		for(int i = 0; i<9; i++) {
			height[i] = Integer.parseInt(br.readLine());
			sum += height[i];
		}
		Arrays.sort(height);
		int wrongdwarf1 = 0;
		int wrongdwarf2 = 0;
		for(int i = 0; i<9; i++) {
			for(int j = 0; j<9; j++) {
				if(sum - (height[i] + height[j]) == 100) {
					wrongdwarf1 = i;
					wrongdwarf2 = j;
					break;
				}
			}
		}
		
		for(int k = 0; k<9; k++) {
			if(wrongdwarf1 == k || wrongdwarf2 == k) {
				continue;
			}
			System.out.println(height[k]);
		}
	}
}
