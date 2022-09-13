package firstclass;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;

public class Main_1158 {

	public static void main(String[] args) {
		
		Queue<Integer> q = new LinkedList<Integer>();
		List<Integer> list = new ArrayList<Integer>();
		
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int k = sc.nextInt();
		
		for(int i = 1; i<=n; i++) {
			q.add(i);
		}
		
		while(!q.isEmpty()) {          //Queue 가 빌때까지 반복
			for(int i = 0; i<k-1; i++) {
				q.add(q.poll());          //poll() : Queue의 맨 앞 숫자를 추출하고 리스트에서 해당 값을 제거
			}                                //q의 맨 뒤에 poll로 뽑은 숫자를 더해줌
			list.add(q.poll());           //q.poll()로 뽑은 Queue의 맨 앞 숫자를 새로운 list에 추가
		}
		System.out.println(list);
		
		
		
		
	}

}
