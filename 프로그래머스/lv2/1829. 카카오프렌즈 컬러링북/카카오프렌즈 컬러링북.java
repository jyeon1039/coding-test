import java.util.*;

class Point{
    int r;
    int c;
    
    Point(int r, int c){
        this.r = r;
        this.c = c;
    }
    
    public int getRow() { return r; }
    public int getColumn() { return c; }
}

class Solution {
    int[] dr = {-1, 1, 0, 0};
    int[] dc = {0, 0, -1, 1};
    
    public int bfs(int[][] picture, int r, int c, int m, int n) {
        Queue<Point> queue = new LinkedList<Point>();
        int target = picture[r][c];
        int area = 0;
        queue.offer(new Point(r, c));
        
        while(!queue.isEmpty()){
            Point p = queue.poll();
            
            for(int i=0; i<4; i++){
                int nr = p.getRow() + dr[i];
                int nc = p.getColumn() + dc[i];
                
                if((0 <= nr && nr < m) && (0 <= nc & nc < n) && (picture[nr][nc] == target)){
                    queue.offer(new Point(nr, nc));
                    picture[nr][nc] = 0;
                    area++;
                }
            }
        }
        
        return area;
    }
    
    public int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;

        for(int r=0; r<m; r++){
            for(int c=0; c<n; c++){
                if(picture[r][c] != 0){
                    numberOfArea++;
                    int sizeOfOneArea = bfs(picture, r, c, m, n);
                    
                     if(maxSizeOfOneArea < sizeOfOneArea)
                         maxSizeOfOneArea = sizeOfOneArea; 
                }
            }
        }
        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }
}