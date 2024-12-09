![image](https://github.com/user-attachments/assets/23bc7fd0-4e43-4abb-ac0f-7c14c9dad631)



배열의 각 원소는 0-9
연속적으로 나타난다면, 하나만 남기고 전부 제거.
제거후 남은 수는 arr의 순서를 유지해야함.

일단, 반복문으로 arr을 순회.
idx가 0일 때는 answer에 추가.
0 이상일 때는 arr[i]와 arr[i-1]을 비교.
다르면 answer에 추가.

```python
def solution(arr):

    answer = []
    
    for i in range(len(arr)):
        if i == 0 or arr[i] != arr[i-1]:
            answer.append(arr[i])

    return answer
```
