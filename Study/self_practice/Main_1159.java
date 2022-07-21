package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main_1159 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		int alphabet[] = new int[26];
		
		for(int i = 0; i<N; i++) {
			String str = br.readLine();
			alphabet[str.charAt(0)-97]++;          //'a' -> 97이므로 charAt(0) - 97로 인덱스 0부터 모두 조사할 수 있게 해 줌.
		}
		
		boolean check = false;
		for(int j = 0; j<26; j++) {
			if(alphabet[j] >= 5) {
				check = true;
				System.out.print((char)(j+97));
			}
		}
		
		if(check == false){
				System.out.println("PREDAJA");
		}
		
	}
}
