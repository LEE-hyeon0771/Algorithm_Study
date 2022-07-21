package fourthclass;
import java.util.*;
public class Main_programmers2_Set {

	    public boolean solution(String[] phone_book){
	        Set<String> set = new HashSet<String>();
	        for(int i = 0; i<phone_book.length; i++){
	            set.add(phone_book[i]);
	        }
	        
	        for(String str : set){
	            for(int j = 0; j<str.length(); j++){
	                if(set.contains(str.substring(0,j))){
	                    return false;
	                }
	            }
	        }
	        return true;
	    }
}
