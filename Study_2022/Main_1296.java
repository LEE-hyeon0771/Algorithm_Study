package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main_1296 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String name = br.readLine();         //연두 이름 
		
		int N = Integer.parseInt(br.readLine());
		String teamName[] = new String[N];   //팀 이름
		int maxName[] = new int[N];          //max 팀 확률값
		
		for(int i = 0; i<N; i++) {           //팀 이름을 N개 입력 받기
			teamName[i] = br.readLine();
		}
		
		Arrays.sort(teamName);
		
		int max = 0;
		for(int i = 0; i<N; i++) {           //팀 이름을 비교해서 max인 팀 이름 확률을 max 변수에 담기
			maxName[i] = maxName(name, teamName[i]);
			if(maxName[i] > max) {
				max = maxName[i];
			}
		}
		
		for(int i = 0; i<N; i++) {
			if(max == maxName[i]) {
				System.out.println(teamName[i]);
				break;
			}
		}
	}
		public static int maxName(String name, String teamName) {
		int L = 0;
		int O = 0;
		int V = 0;
		int E = 0;
		
			for(int i = 0; i<name.length(); i++) {
				if(name.charAt(i) == 'L') {
					L++;
				}
				else if(name.charAt(i) == 'O') {
					O++;
				}
				else if(name.charAt(i) == 'V') {
					V++;
				}
				else if(name.charAt(i) == 'E'){
					E++;
				}
			}
			
			for(int i = 0; i<teamName.length(); i++) {
				if(teamName.charAt(i) == 'L') {
					L++;
				}
				else if(teamName.charAt(i) == 'O') {
					O++;
				}
				else if(teamName.charAt(i) == 'V') {
					V++;
				}
				else if(teamName.charAt(i) == 'E'){
					E++;
				}
			}
		int probable = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100;
		
		return probable;
	}
		
}
		
	


