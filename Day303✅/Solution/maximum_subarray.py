def maximum_subarray(numbers):
    max_sum = numbers[0]
    curr_sum = 0

    for num in numbers:
        if curr_sum < 0:
            curr_sum = 0
        
        curr_sum += num 
        max_sum = max(max_sum, curr_sum)
    
    return max_sum