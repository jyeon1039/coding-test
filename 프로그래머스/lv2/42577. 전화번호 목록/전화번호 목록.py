def solution(phone_book):
    hashmap = {}
    for x in phone_book:
        hashmap[x] = 1
    
    for x in phone_book:
        tmp = ""
        for i in x:
            tmp += i
            if tmp == x:
                break
            if tmp in hashmap and hashmap[tmp] == 1:
                return False
            
    return True