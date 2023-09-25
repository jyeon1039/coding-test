class Solution {
    public String solution(String m, String[] musicinfos) {
        String answer = "(None)";
        int maxMinute = 0;
        m = m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a");
        
        for(String muisc : musicinfos) {
            String[] info = muisc.split(",");
            String title = info[2];
            String code = info[3].replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a");
            int diff = diffTime(info[0], info[1]);
            StringBuilder playCode = new StringBuilder();
            for(int i = 0; i<diff; i++){
                playCode.append(code.charAt(i%code.length()));
            }
            
            if(playCode.toString().contains(m) && diff > maxMinute){
                    maxMinute = diff;
                    answer = title;
            }
        }
        
        return answer;
    }
    
    public int diffTime(String sTime, String eTime){
        String[] st = sTime.split(":");
        String[] et = eTime.split(":");
        int sh = Integer.parseInt(st[0]);
        int sm = Integer.parseInt(st[1]);
        int eh = Integer.parseInt(et[0]);
        int em = Integer.parseInt(et[1]);
        return (eh*60 + em) - (sh*60 + sm);
    }
}