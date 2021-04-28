def solution(answers):
    answer = []
    student1 = [1,2,3,4,5]*int(len(answers)/5+1)
    student2 = [2,1,2,3,2,4,2,5]*int(len(answers)/8+1)
    student3 = [3,3,1,1,2,2,4,4,5,5]*int(len(answers)/10+1)
    count1 = 0
    count2 = 0
    count3 = 0
   
    
    for i in range(len(answers)):
        if (answers[i]==student1[i]):
            count1=count1+1
        if (answers[i]==student2[i]):
            count2=count2+1
        if (answers[i]==student3[i]):
            count3=count3+1
    cnt = [count1, count2, count3]
    for i in range(3):
        if cnt[i] ==max(cnt):
            answer.append(i+1)
       
    

    

    return answer

# list 는 곱셈이 된다.
# max(list)
# 깔끔한 코드는 아직 이해할 수 있는 수준이 아니다.
