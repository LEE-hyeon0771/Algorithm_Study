package fourthclass;
import java.util.*;
public class Main_programmers2_Map {
	    public boolean solution(String[] phone_book){
	        Map<String, Integer> map = new HashMap<String, Integer>();
	        
	        for(int i = 0; i<phone_book.length; i++){
	            map.put(phone_book[i], i);
	        }
	        for(String str : phone_book){
	            for(int j = 0; j<str.length(); j++){
	                if(map.containsKey(str.substring(0,j))){
	                    return false;
	                }
	            }
	        }
	        return true;
	    }
	}

