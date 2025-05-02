# 1에서 16까지 오름차순으로 정렬되어 있는 배열이 있다. 이 배열 내에 14가 존재한다면 True, 존재하지 않는다면 False 를 반환하시오.

finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# 처음 : 1 ... N
# 1번 탐색 : 1 ... N/2 (Down)
# 2번 탐색 : 1 ... N/4 (Down)
# 3번 탐색 : 1 ... N/8 (Down)
# K번 탐색 : 1 ... N/2^K
# K번 탐색하면 N/2^K개가 남는다. N/2^K -> 1이 되려면,
# N = 2^K
# log_2(N) = K

# 시간복잡도 : O(log(N))
def is_existing_target_number_binary(target, array):
    find_count = 0
    cur_min = 0
    cur_max = len(array) - 1
    half = (cur_max + cur_min) // 2
    
    while cur_min <= cur_max:
        find_count += 1
        
        if array[half] == target:
            print(find_count)
            return True
        elif array[half] < target:
            cur_min = half + 1
        else: # array[half] > target
            cur_max = half - 1
        
        half = (cur_max + cur_min) // 2
    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)