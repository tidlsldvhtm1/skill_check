def solution(phone_number):
    answer = ''
    for i in range(1,len(phone_number)-3,1):
        answer = answer + "*"
    for i in range(len(phone_number)-4,len(phone_number),1):
        answer = answer + phone_number[i]

    return answer

# 문자열 관련 함수가 많다.

def hide_numbers(s):
    return "*"*(len(s)-4) + s[-4:]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : " + hide_numbers('01033334444'));

# 문자열 곱셈 가능, s[-4:] <-- 알아두기
