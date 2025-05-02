# https://school.programmers.co.kr/learn/courses/30/lessons/43165

# numbers = [1, 1, 1, 1, 1]
# target_number = 3
# 정답은 5

numbers = [4, 1, 2, 1]
target_number = 4
# 정답은 2


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    all_ways = []

    def all_plus_or_minus(array, cur_index, cur_sum):
        if cur_index == len(array):
            all_ways.append(cur_sum)
            return
    
        all_plus_or_minus(array, cur_index + 1, cur_sum + array[cur_index])
        all_plus_or_minus(array, cur_index + 1, cur_sum - array[cur_index])
        
    all_plus_or_minus(array, 0, 0)
    
    target_count = 0
    
    for way in all_ways:
        if target == way:
            target_count += 1

    return target_count

print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))