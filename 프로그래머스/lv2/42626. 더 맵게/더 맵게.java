import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        Queue<Integer> pq = new PriorityQueue<Integer>();
        
        for(int s : scoville){
            pq.offer(s);
        }
        
        while (pq.peek() < K){
            answer++;
            int s1 = pq.poll();
            int s2 = pq.poll();
            pq.offer(s1 + s2*2);
            
            if(pq.size() == 1 && pq.peek() < K)
                return -1;
        }
        
        return answer;
    }
}