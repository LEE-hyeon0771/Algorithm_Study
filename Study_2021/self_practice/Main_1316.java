package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main_1316 {
	public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	public static void main(String[] args) throws NumberFormatException, IOException {
		
		int N = Integer.parseInt(br.readLine());
		int count = 0;
		for(int i = 0; i<N; i++) {
			if(checkAlpha() == true) {
				count++;
			}
		}
		System.out.println(count);
		
	}
	
	public static boolean checkAlpha() throws IOException {
		String str = br.readLine();
		
		boolean[] alpha = new boolean[26];         //알파벳 담은 배열
		int prevAlpha = 0;                         //이전 알파벳
		
		for(int i = 0; i<str.length(); i++) {
			int nowAlpha = str.charAt(i);            //체크할 현재 알파벳
			
			if(prevAlpha != nowAlpha) {              //현재 알파벳이랑 이전 알파벳이 다른 경우
				if(alpha[nowAlpha - 97] == false) {  //이전에 나온적 없음(false)
					alpha[nowAlpha - 97] = true;     //하나의 그룹이 되므로 true 입력
					prevAlpha = nowAlpha;            //현재 알파벳을 이전 알파벳에 입력하고 다음꺼 체크할 수 있게
				}
				else {                      //이전에 나온적 있음(그룹 단어 아니므로 false를 반환)
					return false;
				}
			}
		}
		return true;    //boolean배열은 기본값이 false이므로 문자열이 그룹단어면 최종적으로 true를 반환
	}

}
