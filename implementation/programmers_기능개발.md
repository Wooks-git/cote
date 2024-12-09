![image](https://github.com/user-attachments/assets/93af26f9-b211-4cbd-9657-148f080bfe31)



100-progresses[i]를 result에 저장.

result%speeds[i] == 0 이면, days에 int(result/speeds[i])

result%speeds[i] != 0 이면, days에 int(result/speeds[i])+1

days 순회.


```python

def solution(progresses, speeds):
    answer = []
    days = []

    # 각 작업이 완료되는데 필요한 날짜 계산
    for i in range(len(progresses)):
        result = 100 - progresses[i]
        if result % speeds[i] == 0:
            days.append(result // speeds[i])
        else:
            days.append(result // speeds[i] + 1)

    max_day = days[0]  
    count = 1  

    for i in range(1, len(days)):
        if days[i] <= max_day:  
            count += 1
        else:  
            answer.append(count)
            max_day = days[i]
            count = 1

    answer.append(count)

    return answer

    
```
