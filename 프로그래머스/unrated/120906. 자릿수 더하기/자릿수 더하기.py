def solution(n):
    answer = 0
    for i in range(len(str(n))):
        answer = answer + int(str(n)[i])
    return answer