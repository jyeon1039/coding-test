import re

def solution(new_id):
    answer = ''
    answer = re.sub('[^a-z\d\-\_\.]', '',new_id.lower()) # 1-2단계: 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
    answer = re.sub('\.\.+', '.', answer) # 3단계: 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    answer = re.sub('^\.', '', answer) # 4단계: 마침표(.)가 처음이나 끝에 위치한다면 제거 => 뒤에서 또 .을 제거할 것이므로 앞의 .들만 제거
    
    if answer == '': # 5단계
        answer = 'a'
    
    answer = re.sub('\.$', '', answer[:15]) # 6단계: 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거, 끝에 위치한 마침표(.) 문자를 제거
    
    if len(answer) <= 2: # 길이가 2자 이하라면, 마지막 문자를 길이가 3이 될 때까지 반복해서 끝에 추가
        while len(answer) < 3:
            answer += answer[-1]
    
    return answer