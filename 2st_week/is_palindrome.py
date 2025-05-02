# https://www.acmicpc.net/problem/17609

input = "abcba"


def is_palindrome(string):
    if len(string) <= 1: # 길이가 1일 때(=마지막 한 글자가 남았을 때)는 회문 검사할 필요없이 True 반환
        return True
    if string[0] != string[-1]: # 맨 앞과 맨 뒤가 다르면 회문이 아니니까 False 반환
        return False
    
    return is_palindrome(string[1:-1]) # 문자열의 맨 앞과 맨 뒤 자르기


print(is_palindrome(input))