package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_2902 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(),"-");      // "-" ������ �ܾ� �ɰ���
		
		StringBuilder sb = new StringBuilder();
		while(st.hasMoreTokens()) {          //"-" �� ������ ��ū(�ܾ�) �� ��ȸ�ϸ鼭 ���� ��ū(�ܾ�) ã��
			String input = st.nextToken();
			sb.append(input.charAt(0));      //�ܾ� �� ���� ó�� ���ڸ� append
		}
		System.out.print(sb);
		
	}

}
