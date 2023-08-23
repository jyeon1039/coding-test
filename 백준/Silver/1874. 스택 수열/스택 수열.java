import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];

        for(int i=0; i<n; i++)
            arr[i] = sc.nextInt();

        int num = 1; // 수열의 수
        Stack<Integer> st = new Stack<>();
        StringBuffer sb = new StringBuffer();

        for(int i=0; i<n; i++){
            int x = arr[i];

            if(x >= num){
                while(x >= num){
                    st.push(num++); // 두 수가 같아질 때까지 push
                    sb.append("+\n");
                }
                st.pop();
                sb.append("-\n");
            }
            else{
                int cur = st.pop();

                if(cur > x){ // 마지막으로 뽑은 수가 수열의 수와 같이 않을 경우 NO 출력
                    System.out.println("NO");
                    return;
                }
                else{
                    sb.append("-\n");
                }
            }
        }

        System.out.println(sb.toString());
    }
}