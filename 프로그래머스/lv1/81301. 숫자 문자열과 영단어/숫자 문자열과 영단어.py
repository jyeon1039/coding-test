def solution(s):
    answer = ""
    
    num = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
          "six": "6", "seven": "7", "eight": "8", "nine": "9", "ten": "10"}
    
    tmp = ""
    for i in range(len(s)):
        x = s[i]
        if "0" <= x and x <= "9":
            answer += x
        else:
            tmp += x
            if tmp in num:
                answer += num[tmp]
                tmp = ""
                
    return int(answer)