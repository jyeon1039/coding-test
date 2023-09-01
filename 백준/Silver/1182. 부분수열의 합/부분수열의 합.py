
n, s = map(int ,input().split())
arr = list(map(int, input().split()))
result = 0

def subset_sum(idx, sub_sum):
    global result
    
    if idx >= n:
        return

    sub_sum += arr[idx]
    
    if sub_sum == s:
        result += 1

    # 현재의 idx를 포함하지 않는 수열
    subset_sum(idx+1, sub_sum-arr[idx])

    # 현재의 idx를 포함하는 수열
    subset_sum(idx+1, sub_sum)

subset_sum(0, 0)
print(result)
