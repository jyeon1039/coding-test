import java.util.*;

class Solution {
    public long getSum(int[] queue){
        int sum = 0;
        for(int i=0; i<queue.length; i++)
            sum += queue[i];
        
        return sum;
    }
    
    public int solution(int[] queue1, int[] queue2) {
        int answer = 0;
        long sum1 = getSum(queue1);
        long sum2 = getSum(queue2);
        Queue<Integer> q1 = new LinkedList<>();
        Queue<Integer> q2 = new LinkedList<>();
        
        for(int i=0; i<queue1.length; i++){
            q1.add(queue1[i]);
            q2.add(queue2[i]);
        }
        
        while(sum1 != sum2){
            if(answer > queue1.length * 4){
                answer = -1;
                break;
            }
            if(sum1 > sum2){
                int x = q1.poll();
                q2.add(x);
                sum1 -= x;
                sum2 += x;
            }
            else{
                int x = q2.poll();
                q1.add(x);
                sum1 += x;
                sum2 -= x;
            }
            
            answer++;
        }
        
        return answer;
    }
}