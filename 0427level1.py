def solution(participant, completion):
    answer = ''
    temp = list(set(participant)-set(completion))
    if len(temp)!=0:
        return temp[0]
    participant.sort()
    completion.sort()
    for i in range(0,len(completion),1):
        if(participant[i]!=completion[i]):
            return participant[i]

# for 문을 이용해 list의 원소를 하나씩 빼는 방법을 사용하면 시간복잡도 증가
# 효율성 면에서 10점
# set은 중복값이 없는 집합의 개념 (?)
# 반드시 다시 풀어볼 것
