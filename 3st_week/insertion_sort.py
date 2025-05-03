# 다음과 같이 숫자로 이루어진 배열이 있을 때, 오름차순으로 삽입 정렬을 이용해서 정렬하시오.

input = [4, 6, 2, 9, 1]

def insertion_sort(array):
    n = len(array)
    
    # O(N^2)
    for i in range(1, n):
        for j in range(i):
            if array[j-i] < array[j-i-1]:
                array[j-i], array[j-i-1] = array[j-i-1], array[j-i]
            else:
                break
    
    # for i in range(n):
    #     for j in range(1, n):
    #         if array[j-1] > array[j]:
    #             array[j-1], array[j] = array[j], array[j-1]
    #         else:
    #             break
            
    return array


insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [4, 5, 7, 7, 8] / 현재 풀이 값 = ",insertion_sort([5,8,4,7,7]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",insertion_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",insertion_sort([100,56,-3,32,44]))