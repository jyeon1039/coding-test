import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[][] arr = new int[N+1][N+1];

        for(int r=1; r<=N; r++){
            st = new StringTokenizer(br.readLine());
            for(int c=1; c<=N; c++)
                arr[r][c] = Integer.parseInt(st.nextToken());
        }

        int[][] s = new int[N+1][N+1];

        // 구간 합 구하기
        for(int r=1; r<=N; r++){
            for(int c=1; c<=N; c++){
                s[r][c] = s[r-1][c] + s[r][c-1] - s[r-1][c-1] + arr[r][c];
            }
        }

        for(int i=0; i<M; i++){
            st = new StringTokenizer(br.readLine());
            int r1 = Integer.parseInt(st.nextToken());
            int c1 = Integer.parseInt(st.nextToken());
            int r2 = Integer.parseInt(st.nextToken());
            int c2 = Integer.parseInt(st.nextToken());

            int result = s[r2][c2] - s[r1-1][c2] - s[r2][c1-1] + s[r1-1][c1-1];
            System.out.println(result);
        }
    }
}
