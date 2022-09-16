package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main_2231 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		for(int i = 1; i<N; i++) {       //�����ڸ� N���ʿ��� ��� üũ
			int num = i;  //������ ���� ����
			int sum = i;   //������ ���� sum�� ������ �� i�� �ְ� �� ����
			while(num != 0) {
				sum = sum + (num % 10);  //198 % 10 = 8, 19 % 10 = 9, 1 % 10 = 1   (198 + 8 + 9 + 1)
				num = num/10;         //198 / 10 = 19, 19 / 10 = 1 
			}
			
			if(sum == N) {      //ã�� �������� �������� �Է� ���� ���� ��ġ�ϸ� ��� ������ �ְ� �ݺ��� ���� -> �ּ� ������
				System.out.println(i);
				return;
			}
		}
		System.out.println(0);
	}
}
