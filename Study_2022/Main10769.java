package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main10769 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String str = br.readLine();
		
		int happycount = str.length() - str.replace(":-)","").length();
		int sadcount = str.length() - str.replace(":-(","").length();
		
		String emo = "";
		if(happycount == 0 && sadcount == 0) {
			emo = "none";
		}
		else if(happycount == sadcount) {
			emo = "unsure";
		}
		else if(happycount > sadcount) {
			emo = "happy";
		}
		else {
			emo = "sad";
		}
		
		System.out.println(emo);
	}
}
