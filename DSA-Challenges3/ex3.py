def valid_parentheses(text):
    stack = []
    
    mapping = {")": "(", "]": "[", "}": "{"}
    
    for char in text:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        elif char in mapping.values():
            stack.append(char)
            
    return len(stack) == 0

print(valid_parentheses("{[()]y}")) 
print(valid_parentheses("([)]"))     
print(valid_parentheses("((()))"))   
print(valid_parentheses("{[}"))      