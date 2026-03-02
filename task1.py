def filter_numbers(numbers, threshold=0, greater=True):
    if greater:
        return [num for num in numbers if num > threshold]
    else:
        return [num for num in numbers if num < threshold]