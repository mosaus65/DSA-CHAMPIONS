def two_sum(numbers, target):
    
    seen = {}
    
    for i, num in enumerate(numbers):
        
        complement = target - num
        
        if complement in seen:
            return [seen[complement], i]
        
        seen[num] = i
    
    return None

print(two_sum([2, 7, 11, 15], 9))  
print(two_sum([3, 2, 4], 6))       
print(two_sum([1, 2, 3], 10))      