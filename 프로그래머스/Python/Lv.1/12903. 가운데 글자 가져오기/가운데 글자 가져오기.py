def solution(s):
    if len(s)/2 == int(len(s)/2):
        return s[int(len(s)/2)-1:int(len(s)/2)+1]
    else:
        return s[len(s)//2]
    
    