def solution(x, n):
    if x>0:
        return [i for i in range(x,(x*n)+1,x)]
    elif x==0:
        return [0]*n
    else:
        x = abs(x)
        return [i*-1 for i in range(x,(x*n)+1,x)]