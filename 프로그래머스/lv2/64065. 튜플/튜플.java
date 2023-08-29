import java.util.*;

class Solution {
    public int[] solution(String s) {
        String[] tuple = s.substring(2, s.length()-2).split("\\}\\,\\{");
        Set<Integer> set = new LinkedHashSet<>(); // 순서를 보장하고 싶을 땐 HashSet 말고 LinkedHashSet을 사용
        Arrays.sort(tuple, (a, b) -> (a.length()-b.length()));
        
        for(String data: tuple){
            String[] arr = data.split(",");
            for(String x: arr)
                set.add(Integer.parseInt(x));
        }
        
        int idx = 0;
        int[] answer = new int[set.size()];
        for(Integer x: set)
            answer[idx++] = x;
        
        return answer;
    }
}