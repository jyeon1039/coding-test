def diffMinute(sTime, eTime):
    sh, sm = map(int, sTime.split(":"))
    eh, em = map(int, eTime.split(":"))
    return (eh*60 + em) - (sh*60 + sm)

# ABC와 ABC# 조심
def solution(m, musicinfos):
    answer = '(None)'
    maxMinute = 0
    m = m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
    
    for music in musicinfos:
        sTime, eTime, title, code = music.split(",")
        code = code.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
        diff = diffMinute(sTime, eTime)
        playCode = ''
        for i in range(diff):
            playCode += code[i%len(code)]
        if m in playCode:
            if diff > maxMinute:
                maxMinute = diff
                answer = title
        
    return answer