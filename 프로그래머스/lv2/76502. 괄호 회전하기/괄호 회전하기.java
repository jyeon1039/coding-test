import java.util.*;

class Solution {
    // 괄호 유효성 검사
    public int isValid(String s){
        Stack<Character> st = new Stack<>();
        
        for (int i=0; i<s.length(); i++){
            char c = s.charAt(i);
            if (c == '(' || c == '[' || c == '{')
                st.push(c);
            else {
                if(st.isEmpty())
                    return 0;
                char x = st.pop();
                if (c == ')' && x != '(')
                    return 0;
                else if (c == ']' && x != '[')
                    return 0;
                else if (c == '}' && x != '{')
                    return 0;
            }
        }
        
        // 괄호가 다 닫히지 않은 경우
        if(!st.isEmpty())
            return 0;
        
        return 1;
    }
    
    public int solution(String s) {
        int answer = 0;
        StringBuilder sb = new StringBuilder();
        
        // 왼쪽으로 회전
        for(int i=0; i<s.length(); i++){
            String tmp = s.substring(i, s.length()) + s.substring(0, i);
            answer += isValid(tmp);
        }
        
        return answer;
    }
}