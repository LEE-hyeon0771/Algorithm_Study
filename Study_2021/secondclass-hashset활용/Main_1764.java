package secondclass;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.StringTokenizer;

class Main_1764 {
    public static void main(String[] args) throws Exception {
       BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
       BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
       int n = Integer.parseInt(st.nextToken());     //듣도 못한 사람
       int m = Integer.parseInt(st.nextToken());     //보도 못한 사람
       
       Set<String> set = new HashSet<String>();           //듣도 못한 사람 넣을 Set - 넣을때 중복되면 알아서 없어지므로 set이 유리함
       List<String> list = new ArrayList<String>();       //듣도 보도 못한 사람 넣어서 출력할 List
       
       for(int i = 0; i<n; i++) {                         //듣도 못한 사람을 입력받은 만큼 set에 추가
    	   set.add(br.readLine());
       }
       for(int j = 0; j<m; j++) {             //보도 못한 사람 만큼 입력받은 사람을 bufferReader로 묶어서 한꺼번에 str에 넣어줌
    	   String str = br.readLine();                                                   
    	   if(set.contains(str)) {            //str에 있는 문자열이 set에 있으면 정답 출력용 list에 담아줌.
    		   list.add(str);
    	   }
       }
       
       Collections.sort(list);         //list를 오름차순으로 정렬
       
       bw.write(list.size() + "\n");
       for(String result : list) {
          bw.write(result + "\n");
       }
        bw.flush();
        br.close();
        bw.close();
    }
}