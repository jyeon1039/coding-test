def solution(cacheSize, cities):
    answer = 0
    cache = []
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.pop(cache.index(city))
            cache.append(city.lower())
            answer += 1
        else:
            if cacheSize != 0:
                if len(cache) == cacheSize:
                    cache.pop(0)
                cache.append(city.lower()) 
            answer += 5
    
    return answer