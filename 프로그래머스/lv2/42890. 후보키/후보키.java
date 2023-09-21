import java.util.*;

class Solution {
    boolean[] visited;
    int rows, cols;
    Set<String> combi = new HashSet<>();
    ArrayList<String> answer = new ArrayList<>();
    
    public int solution(String[][] relation) {
        rows = relation.length;
        cols = relation[0].length;
        visited = new boolean[cols];

        for(int i=1; i<=cols; i++){
            combinations(0, i, relation);
            unique(relation);
            combi.clear();
        }
        return answer.size();
    }
    
    public void combinations(int start, int depth, String[][] relation){
        if(depth==0){
            StringBuilder temp = new StringBuilder();
            
            for(int i=0; i<cols; i++){
                if(visited[i])
                    temp.append(i);
            }
            
            combi.add(temp.toString());
            return;
        }
        
        for(int i=start; i<cols; i++){
            if(!visited[i]){
                visited[i] = true;
                combinations(start+1, depth-1, relation);
                visited[i] = false;
            }
        }
    }
    
    public void unique(String[][] relation){
        for(String data: combi){
            String[] idxs = data.split("");
            Set<String> set = new HashSet<>();
            for(int r=0; r<rows; r++){
                StringBuilder temp = new StringBuilder();
                for(String idx: idxs){
                    int c = Integer.parseInt(idx);
                    temp.append(relation[r][c]);
                }
                set.add(temp.toString());
            }
        
            if(set.size() == rows){ // 유일성 확인
                boolean isUnique = true;
                for(String a : answer){ // 최소성 확인
                    int cnt = 0;
                    String[] answers = a.split("");
                    for(String idx: answers){
                        if(data.contains(idx))
                            cnt++;
                    }
                    
                    if(cnt == a.length()){
                        isUnique = false;
                    }
                }
                
                if(isUnique)
                    answer.add(data);
            }
        }
    }
}