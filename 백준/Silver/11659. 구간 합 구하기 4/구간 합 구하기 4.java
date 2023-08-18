import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bufferedReader.readLine());
        int suNo = Integer.parseInt(st.nextToken());
        int quizNo = Integer.parseInt(st.nextToken());
        long[] S = new long[suNo + 1]; // 인덱스와 숫자를 맞추기 위해 +1만큼 저장
        st = new StringTokenizer(bufferedReader.readLine());
        for(int i=1; i <= suNo; i++) {
            S[i] = S[i-1] + Integer.parseInt(st.nextToken());
        }

        for(int i=0; i<quizNo; i++){
            st = new StringTokenizer(bufferedReader.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            System.out.println(S[e] - S[s-1]);
        }

    }
}
