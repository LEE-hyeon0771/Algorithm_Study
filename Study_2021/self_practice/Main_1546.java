package selftest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_1546 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		double score[] = new double[N];
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		double max = -1.0;
		double sum = 0.0;
		for(int i = 0; i<score.length; i++) {
			score[i] = Double.parseDouble(st.nextToken());
			
			if(score[i] > max) {
				max = score[i];
			}
			
			sum += score[i];
		}
		double average = ((sum/max) * 100) / N;
		System.out.println(average);
	}

}
