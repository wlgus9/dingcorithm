# https://www.acmicpc.net/problem/1929
# 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환하시오. 
# 소수는 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수이다.

input = 20

def find_prime_list_under_number(number):
    prime_list = []
    
    for n in range(2, number+1): # 2부터 20까지 순회
        for i in prime_list: # 소수 순회
            if i*i <= n and n % i == 0:
                break
        else:
            prime_list.append(n)
        
    return prime_list


result = find_prime_list_under_number(input)
print(result)