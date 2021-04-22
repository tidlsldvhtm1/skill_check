def solution(s): 
    if len(s) == 4:
        answer= s.isdigit() # str.isdigit => True or False
    elif len(s)==6:
        answer=s.isdigit()
    else:
        answer=False
    return answer

#다른 풀이 중 가장 눈에 띄는 코드
def string46(s):
    return s.isdigit() and (len(s)==4 or len(s)==6)
