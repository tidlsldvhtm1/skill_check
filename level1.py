def solution(num):
    count = 0
    while count < 500 :
        if num == 1 :
            break
        if num % 2 == 0 :
            num = num/2
            count = count + 1
        
        elif num % 2 == 1 :
            num = num * 3 + 1
            count = count + 1
    if count == 500 :
        answer = -1
    else :
        answer = count
    return answer
