package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_1173 {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int T = Integer.parseInt(st.nextToken());
		int R = Integer.parseInt(st.nextToken());
		
		int exercise = 0; //운동 시간
		int time = 0;  //흐르는 시간
		int X = m; //초기 맥박 
		
		while(exercise < N) {
			if(X+T <= M) {   //운동할 때 
				exercise++;
				X+=T;
			}
			else {  //휴식할 때
				if(X-R < m) {
					X = m;
				}
				else {
					X-=R;
				}
			}
			time++;
			
			if((X+T > M) && (X == m)) {
				System.out.println(-1);
				return;
			}
		}
		System.out.println(time);
	}
}
