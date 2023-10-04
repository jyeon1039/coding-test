import java.util.*;

class Solution {
    int[] answer;
    HashMap<String, String> parent = new HashMap<>();
    HashMap<String, Integer> idx = new HashMap<>();
    
    public void dfs(String seller, int amount){
        if (seller.equals("-"))
            return;
        
        int a = amount / 10;
        answer[idx.get(seller)] += amount - a;
        
        if (a >= 1)
            dfs(parent.get(seller), a);        
    }
    
    public int[] solution(String[] enroll, String[] referral, String[] seller, int[] amount) {
        int n = enroll.length;
        answer = new int[n];
        
        for(int i=0; i<n; i++){
            parent.put(enroll[i], referral[i]);
            idx.put(enroll[i], i);
        }
        
        for(int i=0; i<seller.length; i++)
            dfs(seller[i], amount[i]*100);
        
        return answer;
    }
}