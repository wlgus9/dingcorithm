# 다음과 같이 숫자로 이루어진 배열이 있을 때, 오름차순으로 버블 정렬을 이용해서 정렬하시오.

input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    n = len(array)
    
    # O(N^2)
    for i in range(n - 1): # 마지막 값은 자동으로 정렬되어 있을 거니까 n-1까지만 반복
        for j in range(n - i - 1): # i의 수만큼 정렬이 완료된 상태이니까 -i, 마지막 값 제외 -1
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j] # 위치 바꿔서 정렬
    
    return array

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",bubble_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",bubble_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",bubble_sort([100,56,-3,32,44]))