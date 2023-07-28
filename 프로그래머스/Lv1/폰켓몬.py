def solution(nums):
    answer = 0
    nums_di = {}
    for i in nums:
        if i in nums_di.keys():
            nums_di[i]+=1
        else:
            nums_di[i]=1
    
    answer=min(len(nums_di.keys()), len(nums)//2)
    return answer