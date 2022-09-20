package secondclass;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

public class Main_3052 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		Set<Integer> set = new HashSet<Integer>();
		
		for(int i = 0; i<10; i++) {                                    
			int n = Integer.parseInt(br.readLine());         //set안에서는 중복되면 자동으로 제외되므로 42를 나눈 나머지를 추가만 해주면된다.
			set.add(n%42);
		}
		
		br.close();
		System.out.println(set.size());           //마지막으로 중복된 것이 제외되고 남아 있는 set의 개수를 출력만 하면 끝
	}

}
