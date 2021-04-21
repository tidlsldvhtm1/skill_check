def solution(x):
    num = 0
    arr = str(x)
    for i in range (0,len(arr),1):
        num = num + int(arr[i])

    if x%num == 0 :
        answer = True
    else :
        answer = False



    return answer
