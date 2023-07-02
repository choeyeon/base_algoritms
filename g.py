
nums = [4,5,2,1]
queries = [3,10,12]
def answerQuaries(nums, queries):

    nums.sort()
    ans = []

    for query in queries:
        count = 0
        for num in nums:
            if query >= num:
                query -= num
                count += 1
            else:
                break
        ans.append(count)
        
    return ans
        
        
        

print(answerQuaries(nums, queries))