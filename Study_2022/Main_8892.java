package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class Main_8892 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int N = Integer.parseInt(br.readLine());
		
		for(int i = 0; i<N; i++) {
			int num = Integer.parseInt(br.readLine());
			String arr[] = new String[num];
			boolean bool = false;
			
			for(int j = 0; j<num; j++) {
				arr[j] = br.readLine();
			}
			
			for(int j = 0; j<num; j++) {
				for(int k = 0; k<num; k++) {
					
					String palind = arr[j] + arr[k];
					
					if(Palindrome(palind)) {
						sb.append(palind + '\n');
						bool = true;
						break;
					}
				}
			}
			if(!bool) {
				sb.append(0 +'\n');
			}
		}
		System.out.println(sb.toString());
	}
	
	public static boolean Palindrome(String str) {
		for(int i = 0; i<(str.length())/2; i++) {
			if(str.charAt(i) != str.charAt(str.length() - i - 1)) {
				return false;
			}
		}
		return true;
	}
}
