import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        HashMap<String, Integer> map = new HashMap<String, Integer>();
        for(String number : phone_book)
            map.put(number, 1);
        
        for(String number : phone_book){
                for(int i=0; i<number.length(); i++){ // number.length()를 포함하게 되면 모두 false를 반환
                    if(map.containsKey(number.substring(0, i))){
                        return false;
                    }
                }
        }
        
        return true;
    }
}