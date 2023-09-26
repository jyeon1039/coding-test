import java.util.*;

class Solution {
    public String[] solution(String[] files) {
        Arrays.sort(files, new Comparator<String>() {
            @Override
            public int compare(String s1, String s2){
                String[] file1 = getFileInfo(s1);
                String[] file2 = getFileInfo(s2);
                
                int result = file1[0].compareTo(file2[0]); // head 비교
                
                if(result == 0){ // head가 같을 때
                    int number1 = Integer.valueOf(file1[1]);
                    int number2 = Integer.valueOf(file2[1]);
                    
                    return number1 - number2;
                }
                return result;
            }
            
            public String[] getFileInfo(String file){
                StringBuilder head = new StringBuilder();
                StringBuilder number = new StringBuilder();
                
                int idx = 0;
                
                for(int i=idx; i<file.length(); i++){
                    char ch = file.charAt(i);
                    if ('0' <= ch && ch <= '9'){
                        idx = i;
                        break;
                    }
                    else
                        head.append(ch);
                }
                
                for(int i=idx; i<file.length(); i++){
                    char ch = file.charAt(i);
                    if(!('0' <= ch && ch <= '9')) // 숫자 뒤에 나오는 문자는 tail
                        break;
                    number.append(ch);
                }
                
                String[] fileInfo = {head.toString().toLowerCase(), number.toString()};
                return fileInfo;
            }
        });
        
        return files;        
    }
}