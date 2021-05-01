def solution(n):
    answer = ''
    if(n%2==0):
        answer = "수박"*int(n/2)
    if(n%2==1):
        answer = "수박"*int(n/2)+"수"
    
    return answer
#수박수박수
#쉽게 풀었으나 간단한 코드로 풀어보면
# return "수박"*(n/2) + "수"*(n%2)
