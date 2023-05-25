def solution(genres, plays):
    answer = []
    album = {}
    album_plays = {}
    
    for i in range(len(genres)):
        g = genres[i]
        p = plays[i]
        if g not in album:
            album[g] = []
            album_plays[g] = 0
        album[g].append((i, p))
        album_plays[g] += p
    album_plays = sorted(album_plays.items(), key=lambda x: x[1], reverse=True)
    print(album_plays)

    for g in album.keys():
        album[g].sort(key=lambda x:x[1], reverse=True)
    
    for g in album_plays:
        a = album[g[0]][:2]
        for x in a:
            answer.append(x[0])
        
    return answer