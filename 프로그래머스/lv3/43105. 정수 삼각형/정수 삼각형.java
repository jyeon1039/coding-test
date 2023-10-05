class Solution {
    public int solution(int[][] triangle) {
        int answer = 0;
        int rows = triangle.length;
        int cols = triangle[rows-1].length;
        
        for(int r=1; r<rows; r++){
            for(int c=0; c<=r; c++){
                if (c == 0) // 맨 왼쪽
                    triangle[r][c] += triangle[r-1][c];
                else if(c == r) // 맨 오른쪽
                    triangle[r][c] += triangle[r-1][c-1];
                else{
                    // max(triangle[r-1][c], triangle[r-1][c-1]
                    int x = triangle[r-1][c];
                    if (triangle[r-1][c-1] > x)
                        x = triangle[r-1][c-1];
                    triangle[r][c] += x;                    
                }
            }
        }   
        
        // 최댓값
        for(int c=0; c<cols; c++){
            int x = triangle[rows-1][c];
            if(x > answer)
                answer = x;
        }
        
        return answer;
    }
}