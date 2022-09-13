package firstclass;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main_2605 {

	public static void main(String[] args) {
		
		Scanner input = new Scanner(System.in);
		
		int n = input.nextInt();          //몇 명인지 입력
		
		List<Integer> list = new ArrayList<Integer>();       //담을 arrayList 하나 선언
		
		for(int i = 1; i<=n; i++) {
			int num = input.nextInt();                     //뽑을 번호 입력
			if(num == 0) {                                 //0이면 그대로 이므로 바로 add로 넣어줌
				list.add(i);
			}
			else {
				list.add(list.size() - num, i);           //0아니면 list의 사이즈에서 숫자를 빼줘서 뒤에서 부터 담음
			}                                             //add(k,index) : index에 k 넣는 메소드
		}
		
		for(int i = 0; i<n; i++) {
			System.out.print(list.get(i) + " ");               //넣은 명수 만큼 인덱스를 get메소드로 불러옴
		}
	}

}
