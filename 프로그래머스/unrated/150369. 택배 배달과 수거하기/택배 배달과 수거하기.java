class Solution {
    public long solution(int cap, int n, int[] deliveries, int[] pickups) {
        long answer = 0;
        
        int deliver_n = 0;
        int pick_n = 0;
        
        for(int i=n-1; i>=0; i--){
            deliver_n -= deliveries[i];
            pick_n -= pickups[i];
            
            // 한 번 다녀왔지만 배달해야하거나 수거해야 할 물건이 남아있는 경우 또 가야하므로 while 루프 
            while(deliver_n < 0 || pick_n < 0) { 
                deliver_n += cap;
                pick_n += cap; 
                answer += (i+1)*2;
            }
        }
        
        return answer;
    }
}