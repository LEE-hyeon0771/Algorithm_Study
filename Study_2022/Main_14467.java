package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_14467 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		int[][] arr = new int[11][1];
		
		for(int i = 0; i<11; i++) {   //변수 -1로 초기화
			arr[i][0] = -1;
		}
		
		int count = 0;
		
		for(int i = 0; i<N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			
			int num = Integer.parseInt(st.nextToken());
			int place = Integer.parseInt(st.nextToken());
			
			if(arr[num][0] == -1) {     //position이 0,1이 아닌 초기값에서 그대로면
				arr[num][0] = place;
			}
			else if(arr[num][0] != place) { //position이 해당 값에서 변경될 때
				count++;
				arr[num][0] = place;   //다시 원래 값 설정해주고 반복할 수 있게
			}
		}
		
		System.out.println(count);
	}
}
