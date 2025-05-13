# https://www.acmicpc.net/problem/2493

top_heights = [6, 9, 5, 7, 4]

# O(N^2)
def get_receiver_top_orders(heights):
    result = [0] * len(heights)
    
    # 1. 반복문 이용
    # for i in range(len(heights) - 1, 0, -1):
    #     for j in range(i - 1, -1, -1):
    #         if heights[i] <= heights[j]:
    #             result[i] = j + 1
    #             break
    
    # 2. 스택 이용
    while heights: # height가 비어있지 않을 때까지 반복
        height = heights.pop()
        
        for i in range(len(heights)-1, -1, -1):
            if height <= heights[i]:
                result[len(heights)] = i + 1
                break
        
    return result


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!

print("정답 = [0, 0, 2, 2, 4] / 현재 풀이 값 = ",get_receiver_top_orders([6,9,5,7,4]))
print("정답 = [0, 0, 0, 3, 3, 3, 6] / 현재 풀이 값 = ",get_receiver_top_orders([3,9,9,3,5,7,2]))
print("정답 = [0, 0, 2, 0, 0, 5, 6] / 현재 풀이 값 = ",get_receiver_top_orders([1,5,3,6,7,6,5]))