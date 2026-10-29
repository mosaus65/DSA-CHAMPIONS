def closest_number(numbers, target):
    if not numbers:
        return None

    closest = numbers[0]

    for number in numbers:
        if abs(number - target) < abs(closest - target):
            closest = number
        elif abs(number - target) == abs(closest - target):
            if number < closest:
                closest = number

    return closest


print(closest_number([4, 8, 15, 20], 13))  
print(closest_number([8, 12], 10))        