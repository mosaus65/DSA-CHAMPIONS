def move_zeros(numbers):
    position = 0

    for number in numbers:
        if number != 0:
            numbers[position] = number
            position += 1

    while position < len(numbers):
        numbers[position] = 0
        position += 1

    return numbers

print(move_zeros([0, 1, 0, 3, 12]))       
print(move_zeros([4, 0, 5, 0, 2]))
print(move_zeros([1, 2, 3]))