# DFS 풀이
def solution(numbers, target):
    answer = 0
    
    def dfs(idx, total):
        nonlocal answer
        
        if len(numbers) == idx:
            if total == target:
                answer += 1
            return
        
        dfs(idx+1, total + numbers[idx])
        dfs(idx+1, total - numbers[idx])
    
    dfs(0,0) #  numbers의 첫 번째 idx, total : 순회하면서의 합.
    
    return answer

# stack-over flow 방지를 위한 반복 호출 사용.
def solution(numbers, target):
    answer = 0
    stack = [(0,0)]

    while stack:
        idx, total = stack.pop()
        
        if idx == len(numbers):
            if total == target:
                answer += 1
            continue

        stack.append((idx+1, total + numbers[idx]))
        stack.append((idx+1, total - numbers[idx]))
    
    return answer
