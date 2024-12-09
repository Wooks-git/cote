<img width="490" alt="image" src="https://github.com/user-attachments/assets/3b73b5da-ecf7-4858-9fc9-3226f25b61da">


문자열 s를 돌기.
count = 0으로 시작
만약 ')' 문자로 시작하는 s열이면 answer = False 또한, count가 0이면 () 한 세트가 끝난건데, ')'로 시작하면 틀린 문장임.

만약 '(' 문자로 시작하면, count 1 추가.

```
def solution(s):
    answer = True
    
    count = 0
    
    for i in range(len(s)):
        if count == 0 and s[i]== ')':
            answer = False
            break
            
        elif s[i] == '(':
            count += 1
        
        elif s[i] == ')':
            count -= 1
            
    if count != 0:
        answer = False
        

    return answer
```
