package selftest;

public class ProgrammersKakao2018_1 {
    public int solution(String dartResult) {
        int answer = 0;
        int[] arr = new int[3];
        String temp = "";
        int index = 0;
        int num = 0;
 
        for (int i = 0; i < dartResult.length(); i++) {
            char dart = dartResult.charAt(i);
 
            if (dart >= '0' && dart <= '9') {
                temp += String.valueOf(dart);
            } else if (dart == 'S' || dart == 'D' || dart == 'T') {
                num = Integer.parseInt(temp);
                if (dart == 'S') {
                    arr[index++] = (int)Math.pow(num, 1);
                } else if (dart == 'D') {
                    arr[index++] = (int)Math.pow(num, 2);
                } else {
                    arr[index++] = (int)Math.pow(num, 3);
                }
                temp = "";
            } else {
                if (dart == '#') {
                    arr[index - 1] *= -1;
                } else {
                    arr[index - 1] *= 2;
                    if (index >= 2) {
                       arr[index - 2] *= 2;
                    }
                }
            }
        }
 
        for (int i = 0; i < 3; i++) {
            answer += arr[i];
        }
        return answer;
    }
}