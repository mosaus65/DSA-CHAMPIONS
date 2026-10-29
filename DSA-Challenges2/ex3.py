def balanced_brackets(text):
    stack = []

    opening = "([{"
    closing = ")]}"
    matches = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for char in text:
        if char in opening:
            stack.append(char)

        elif char in closing:
            if not stack:
                return False

            last_opening = stack.pop()
            if last_opening != matches[char]:
                return False

    return len(stack) == 0     

print(balanced_brackets("(hello)" ))
print(balanced_brackets("{[()]}"))
print(balanced_brackets("([)]"))
print(balanced_brackets("((hello)"))