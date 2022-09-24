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
		
		for(int i = 0; i<11; i++) {   //���� -1�� �ʱ�ȭ
			arr[i][0] = -1;
		}
		
		int count = 0;
		
		for(int i = 0; i<N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			
			int num = Integer.parseInt(st.nextToken());
			int place = Integer.parseInt(st.nextToken());
			
			if(arr[num][0] == -1) {     //position�� 0,1�� �ƴ� �ʱⰪ���� �״�θ�
				arr[num][0] = place;
			}
			else if(arr[num][0] != place) { //position�� �ش� ������ ����� ��
				count++;
				arr[num][0] = place;   //�ٽ� ���� �� �������ְ� �ݺ��� �� �ְ�
			}
		}
		
		System.out.println(count);
	}
}
