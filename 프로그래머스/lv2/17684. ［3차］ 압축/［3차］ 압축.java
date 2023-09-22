import java.util.*;

class Solution {
    public int[] solution(String msg) {
        ArrayList<Integer> ans = new ArrayList<>();
        HashMap<String, Integer> dictionary = new HashMap<String, Integer>();
        int dicIdx = 1;
        for(char i='A'; i<='Z'; i++)
            dictionary.put(i+"", dicIdx++);
        
        int idx = 0;
        while (idx < msg.length()){
            int tmpIdx = 0;
            int cnt = 0;
            for (int i = idx+1; i<= msg.length(); i++){
                String tmp = msg.substring(idx, i);
                if (dictionary.containsKey(tmp)){
                    tmpIdx = dictionary.get(tmp);
                    cnt++;
                }
                else{
                    dictionary.put(tmp, dicIdx++);
                    break;
                }
            }
            idx += cnt;
            ans.add(tmpIdx);
        }
                
        int[] answer = new int[ans.size()];
        for(int i=0; i<ans.size(); i++)
            answer[i] = ans.get(i);
        
        return answer;
    }
}