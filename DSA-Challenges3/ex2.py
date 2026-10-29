def longest_consecutive(numbers):
    if not numbers:
        return 0
        
    num_set = set(numbers)
    max_len = 0
    
    for num in num_set:
        if (num - 1) not in num_set:
            current_num = num
            current_streak = 1
            
            while (current_num + 1) in num_set:
                current_num += 1
                current_streak += 1
                
            max_len = max(max_len, current_streak)
            
    return max_len

print(longest_consecutive([100, 4, 200, 1, 3, 2])) 
print(longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  
print(longest_consecutive([]))                      