def reverse_first(queue, k):
    if k < 0 or k > len(queue):
        raise ValueError("k must be between 0 and the queue length")

    stack = []

    for _ in range(k):
        stack.append(queue.pop(0))

    while stack:
        queue.append(stack.pop())

    return queue


print(reverse_first([10, 20, 30, 40, 50], 3))
print(reverse_first([1, 2, 3, 4], 2))