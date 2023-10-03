class Solution {
    public int[] solution(String s) {
        int[] answer = new int[2];
        answer[0] = 0;
        answer[1] = 0;
        while (!s.equals("1")){
            answer[0]++;
            int cnt = 0; // 1의 개수
            for(int i=0; i<s.length(); i++){
                if(s.charAt(i) == '0') // 0의 개수
                    answer[1]++;
                else
                    cnt++;
            }
            s = Long.toString(cnt, 2);
        }

        return answer;
    }
}