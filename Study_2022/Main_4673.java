package selftest;


public class Main_4673 {
	
	public static void main(String[] args) {
	
	final int num = 10001;
	
	boolean arr[] = new boolean[num];
	
	for(int i = 1; i<num; i++) {
		int n = d(i);
		
		if(n < 10001) {
			arr[n] = true;
		}
	}
	
	for(int i = 1; i<num; i++) {
		if(!arr[i]) {
			System.out.println(i);
		}
	}
}
	
	public static int d(int num) {
		int sum = num;
		
		while(num != 0) {
			sum += (num % 10);
			num /= 10;
		}
	return sum;
	}
}


