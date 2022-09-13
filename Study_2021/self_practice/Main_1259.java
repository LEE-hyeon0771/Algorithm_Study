package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main_1259 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		while(true) {
			String str = br.readLine();            //str 입력받기
			
			String arr[] = new String[str.length()];        //str을 문자별로 잘라서 담을 배열
			if(str.equals("0")) {                          //0이면 break
				break;
			}
			for(int i = 0; i<str.length(); i++) {          //str을 substring으로 잘라서 하나씩만 arr배열에 담아줌
				arr[i] = str.substring(i,i+1);                 //type은 String이지만 charAt(i)와 동일한 기능
			}
			
			List<String> list = new ArrayList<String>();  //str을 뒤집어서 담을 list
			
			for(int i = 0; i<str.length(); i++) {
				list.add(arr[str.length()-1-i]);            //list에 str을 뒤집어서 인덱스를 담아줌
			}
			
			int count = 0;
			for(int i = 0; i<str.length(); i++) {
				
				String s = list.get(i);                 //list에 담긴 string 문자 하나를 불러옴
				if(s.contains(arr[i])) {                 //s가 arr[i]에 들어있다면 count++
					count++;
				}
			}
			
			if(count == str.length()) {                 //count가 ++되어서 str의 길이와 똑같다면 펠린드롬수임
				sb.append("yes" + "\n");
			}
			else {
				sb.append("no" + "\n");
			}	
		}
		System.out.println(sb.toString());            //StringBuilder로 담아서 한번에 출력
	}
}
