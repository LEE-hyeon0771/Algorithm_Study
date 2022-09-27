package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main_1296 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String name = br.readLine();         //���� �̸� 
		
		int N = Integer.parseInt(br.readLine());
		String teamName[] = new String[N];   //�� �̸�
		int maxName[] = new int[N];          //max �� Ȯ����
		
		for(int i = 0; i<N; i++) {           //�� �̸��� N�� �Է� �ޱ�
			teamName[i] = br.readLine();
		}
		
		Arrays.sort(teamName);
		
		int max = 0;
		for(int i = 0; i<N; i++) {           //�� �̸��� ���ؼ� max�� �� �̸� Ȯ���� max ������ ���
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
		
	


