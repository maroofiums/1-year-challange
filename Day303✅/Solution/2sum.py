def twosum(numbers, target):
    seen = {}

    for i in range(len(numbers)):
        complement = target - numbers[i]
        if complement in seen:
            return (seen[complement], i)
        seen[numbers[i]] = i
    return None