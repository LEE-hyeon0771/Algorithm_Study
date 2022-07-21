package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_7568 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		int arr[][] = new int[N][2];         //몸무게, 키 입력 받는 배열
		
		for(int i = 0; i<arr.length; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
				
			arr[i][0] = Integer.parseInt(st.nextToken());     // 몸무게
			arr[i][1] = Integer.parseInt(st.nextToken());     // 키
		}
		
		for(int i = 0; i<arr.length; i++) {
			int result = 1;
			for(int j = 0; j<arr.length; j++) {
				if((arr[i][0] < arr[j][0]) && (arr[i][1] < arr[j][1])) {
					result++;
				}
			}
			System.out.print(result + " ");
		}
	}
}
