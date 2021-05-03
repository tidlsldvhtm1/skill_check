def solution(num):
    answer = ''
    if num%2 == 0:
        answer = "Even"
    else:
        answer = "Odd"
    return answer


# 아주 흔한 짝수 홀수 문제
# return num % 2 and "Odd" or "Even"
# num % 2가 거짓(0)이라면 num % 2 ==0 (거짓) and Odd 가 되므로,
# 둘 다 참이어야하는 조건에 맞지 않기 때문에 or Even으로 해서 둘 중에
# 하나라도 참일 때 가능한 Even이 출력되며 , num%2가
# 1(참)이면 and 조건이 성립되어 Odd가 출력됩니다.


 
