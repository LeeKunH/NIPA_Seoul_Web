# ## Task 1
#
#  Create a function that takes in two integers and returns
# a Boolean True if their sum is 10, False if their sum is something else.

'''
1번 풀이는 아래와 같음
    해설을 보니 좀 더 간단하게 축약 가능
    그건 2번 풀이 확인.
'''


def check_ten(n1, n2):
    # Code Here
    if (n1 + n2) == 10:
        return True
    else:
        return False


'''
2번 풀이 아래와 같음
'''


def check_ten(n1, n2):
    # Code Here
    return (n1 + n2) == 10


# 인수의 합이 10이면 True 출력
print(check_ten(5, 5))

# 인수의 합이 10이 아니면 False 출력
print(check_ten(5, 6))


print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")

# ## Task 2
#
# Create a function that takes in two integers and returns True if their
# sum is 10, otherwise, return the actual sum value.


def check_ten_sum(n1, n2):
    # Code Here
    if (n1 + n2) == 10:
        return True
    else:
        return n1 + n2


# 인수의 합이 10이면 True 출력, 아니면 실제 계산된 값을 출력
print(check_ten_sum(5, 5))
print(check_ten_sum(5, 6))

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")


# ## Task 3
#
# Create a function that takes in a string and returns back the
# first character of that string in upper case.

'''
1번 풀이는 아래와 같다.
    해설코드를 보니 굳이 입력한 문자열을 리스트로 변환할 필요가 없었음
    따라서 수정한 코드는 2번 풀이로 작성
'''

# def first_upper(mystring):
#     # Code Here
#     list_mystring = list(mystring)
#     first_char = list_mystring[0]

#     return first_char.upper()

'''
2번 풀이는 아래와 같다.
'''


def first_upper(mystring):
    # Code Here
    return mystring[0].upper()


# 합수에 입력된 문자형 자료형의 첫 글자가 대문자로 반환 출력
print(first_upper('apple'))
print(first_upper('melon'))


print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")


# ## Task 4
#
# Create a function that takes in a string and returns the last two characters.
# If there are less than two chracters, return the string:  "Error".
# Use this link if you need help/hint.
# (https://stackoverflow.com/questions/7983820/get-the-last-4-characters-of-a-string)


'''
1번 풀이는 아래와 같다.
    해설코드를 보니 좀 더 간단하게 작성이 가능했다.
        굳이 문자열을 리스트화 x
        pop메서드 사용하지 않고 슬라이싱으로 처리 가능
    2번 풀이를 확인하자
'''
# def last_two(mystring):
#     # Code Here
#     list_mystring = list(mystring)

#     if (len(list_mystring) >= 2):
#         last_char1 = list_mystring.pop()
#         last_char2 = list_mystring.pop()
#         last_two_str = last_char2 + last_char1

#         return print(last_two_str)

#     else:
#         return print("Error")

'''
2번 풀이는 아래와 같다.
'''


def last_two(mystring):
    if len(mystring) < 2:
        return "Error"
    else:
        return mystring[-2:]


# 문자열 자료형을 입력받는다
# 마지막 두 글자를 반환한다.
# 2글자보다 길이가 짧으면 "Error" 반환한다.
last_two("apple")
last_two("ap")
last_two("p")

print(last_two("apple"))
print(last_two("ap"))
print(last_two("p"))


print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")


# ## Task 5
#
# Given a list of integers, return True if the sequence [1,2,3] is somewhere
# in the list. Hint: Use slicing and a for loop.

'''
1번 풀이는 틀린 풀이임
5번은 시퀀스 용어를 잘 못 이해함
틀림
해설코드를 확인하고 작성함

다양한 풀이 방법 존재
목록의 마지막 두 항목까지 계속 반복하는 방법

연속된 3개의 수가 문제에서 원하는 1 > 2 > 3 인지
시퀀스를 이렇게 확인하는 거구나
0번 > 1번 > 2번 인덱스 확인
    1번 > 2번 > 3번 인덱스 확인
        2번 > 3번 > 4번 인덱스 확인 .....
        => 이렇게 단계적으로 시퀀스를 확인하고 있음

-2를 하는 이유
왜 끝까지 안 가고 ?
생각해보면 당연하다
현재 길이가 3인 시퀀스를 확인하고 있다
따라서 i로 들어오는 인덱스 기준 +1 +2를 확인해야 한다.
그러기 위헤선 전체 길이에서 -2를 해야 범위를 초과하지 않는다.
이해 ㅇㅇㅇ


'''


def seq_check(nums):
    # Code here
    sequence = [1, 2, 3]

    if sequence in nums:
        return print(True)

    else:
        return print(False)


# 정수 목록이 주어지면 [1,2,3] 시퀀스가 어딘가에 있으면 True를 반환
# 리스트에. 힌트: 슬라이싱과 for 루프를 사용

# [1,2,3]시퀀스가 있는 경우
seq_check([1, 2, 3, 4, 5, 6, 7])
# [1,2,3]시퀀스가 없는 경우
seq_check([1, 2, 4, 5, 6, 7, 8, 15])

'''
2번 풀이
해설 코드 기록
'''


def seq_check(nums):

    # Note: iterate with length-2, so can use i+1 and i+2 in the loop
    for i in range(len(nums)-2):
        # Check in sets of 3 if we have 1,2,3 in a row
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False


seq_check([1, 2, 3])
seq_check([7, 7, 7, 1, 2, 3, 7, 7, 7])
seq_check([3, 2, 1, 3, 2, 1, 1, 1, 2, 2, 3, 3, 3])

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")

# ## Task 6
#
# Given a 2 strings, create a function that returns the difference in length
# between them. This difference in length should always be a positive number
# (or just 0). Hint: Absolute Value.**


'''
1번 풀이 =>
무조건 큰 - 작은값이 되도록 작성
'''


def compare_len(s1, s2):
    # Code Here
    num1 = len(s1)
    num2 = len(s2)

    if num1 > num2:
        diff_length = num1 - num2
    else:
        diff_length = num2 - num1

    return print(f'입력된 두 문자열 길이 차이 : {diff_length}')


'''
2번 풀이 =>
작-큰값 되더라도 양수값이 출력되도록 작성
'''


def compare_len(s1, s2):
    return print(f'입력된 두 문자열 길이 차이 : {abs(len(s1)-len(s2))}')


# 입력된 두 문자열 길이 차이
# 값은 항상 양수
# 1번 풀이 큰 - 작은값 뺴던가 or 2번 풀이절대값-함수을 이용하던가
compare_len("starbucks", "coffee")
compare_len("coffee", "starbucks")


print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")


# ## Task 7
#
# Given a list of integers, if the length of the list is an even number,
# return the sum of the list. If the length of the list is odd, return the max
# value in that list.


def sum_or_max(mylist):

    # Code Here
    list_lens = len(mylist)

    if (list_lens % 2 == 0):

        # # sol)1
        # total_sum = 0
        # for num in mylist:
        #     total_sum += num

        # sol)2
        total_sum = sum(mylist)

        return print(f'리스트 길이 짝수! > 총 합 : {total_sum}')

    else:
        max(mylist)
        return print(f'리스트 길이 홀수! > 최대값 : {max(mylist)}')


'''
리스트 길이가 짝수라면
    리스트 요소값들의 합 반환
리스트 길이가 홀수라면
    리스트 값들 중 최대값 반환
'''

# 리스트 길이 짝수 경우 =>
even_num_list = [1, 2, 3, 4, 5, 6]
sum_or_max(even_num_list)
# 리스트 길이 홀수 경우 =>
odd_num_list = [5, 10, 15, 20, 25]
sum_or_max(odd_num_list)
