package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.StringTokenizer;

public class Main_7785 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		Set<String> set = new HashSet<>();
		for(int i = 0; i<N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			
			String name = st.nextToken();
			String report = st.nextToken();
			
			if(report.equals("enter")) {
				set.add(name);
			}
			else {
				set.remove(name);
			}
		}
		
		List<String> list = new ArrayList<String>(set);
		
		Collections.sort(list, Collections.reverseOrder());
		
		for(String value : list) {
			System.out.println(value);
		}
	}
}
