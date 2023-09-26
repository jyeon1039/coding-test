def solution(files):
    answer = []
    result = []
    
    for i, x in enumerate(files):
        alpha = ''
        digit = ''
        for c in x.lower().split('.')[0]:
            if c.isdigit():
                digit += c
                if len(str(int(digit))) == 5: # number는 최대 다섯 글자
                    break # head 뒤에 number이므로 break 가능
            else:
                if len(digit) != 0: # number 뒤에 다시 나오는 문자는 tail 처리
                    break
                alpha += c
        result.append((alpha, int(digit), i)) #(head, number, idx)
    result.sort(key=lambda x: (x[0], x[1])) # head 오름차순 정렬 후, 같으면 number 정렬

    for head, number, idx in result:
        answer.append(files[idx])
        
    return answer