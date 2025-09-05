# Problem: C - Loopix: The Book Cycle - https://codeforces.com/gym/632067/problem/C

 left_index = 0
    right_index = 0
    sorted_subarray = []
   
    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] <= right_half[right_index]:
            sorted_subarray.append(left_half[left_index])
            left_index += 1
        else:
            sorted_subarray.append(right_half[right_index])
            right_index += 1
           
    sorted_subarray.extend(left_half[left_index:])
    sorted_subarray.extend(right_half[right_index:])
   
    return sorted_subarray
