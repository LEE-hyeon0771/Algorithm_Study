package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main_1475 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String N = br.readLine();
		
		int[] arr = new int[10];     //0~9 플라스틱 세트
		int num = 0;
		for(int i = 0; i<N.length(); i++) {
			num = N.charAt(i) - '0';
			if(num == 9) {
				num = 6;
			}
			arr[num]++;
		}
		int temp = arr[6] + arr[9];
		if(temp % 2 == 0) {              //6과 9의 세트의 총합이 짝수면 6,9 만 구분 나누기 2
			arr[6] = temp/2;
		}
		else {
			arr[6] = temp/2 + 1;         //6과 9의 세트의 총합이 홀수면 6,9 구분하고 한 세트가 더 필요
		}
		Arrays.sort(arr);
		
		System.out.println(arr[9]);         
	}

}
