def solution(skill, skill_trees):
    answer = 0

    for tree in skill_trees:
        s = ''
        for c in tree:
            if c in skill:
                s += c

        if s == skill[:len(s)]:
            answer += 1

    return answer