package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main_1100 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[][] chess = new String[8][8];
		int i, j, count=0;
		
		for(i = 0; i<chess.length; i++) {
			String str = br.readLine();
			
			for(j = 0; j<chess.length; j++) {
				chess[i][j] = str.substring(j,j+1);
				
				if((i+j) % 2 == 0 && chess[i][j].equals("F")) {
					count++;
				}
			}
		}
		System.out.println(count);
	}

}
