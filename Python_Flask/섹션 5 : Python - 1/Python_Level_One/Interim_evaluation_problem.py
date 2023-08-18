#####################################
#### PART 6: EXERCISE REVIEW  #######
#####################################

# Time to review all the basic data types we learned! This should be a
# relatively straight-forward and quick assignment.

###############
## Problem 1 ##
###############

# Given the string:
s = 'flask'

# Use indexing to print out the following:
# 'f'
print(s[0])

# 's'
print(s[3])

# 'ask'
# 문자열 슬라이싱 복기
print(s[2:])

# 'las'
print(s[1:4])

# 'k'
print(s[-1])
print(s[4:])
print(s[4])

# Bonus: Use indexing to reverse the string
# 문자열 역순 출력 가능, 음 인덱스 복기
print(s[::-1])


###############
## Problem 2 ##
###############

# Given this nested list:
mylist = [3, 7, [1, 4, 'hello']]
# Reassign "hello" to be "goodbye"
print(mylist[2][2])
mylist[2][2] = 'goodbye'
print(mylist)


###############
## Problem 3 ##
###############

# Using keys and indexing, grab the 'hello' from the following dictionaries:

d1 = {'simple_key': 'hello'}
print(d1['simple_key'])

d2 = {'k1': {'k2': 'hello'}}
print(d2['k1']['k2'])

d3 = {
    'k1': [{'nest_key': ['this is deep', ['hello']]}]
}


'''
# 현 상황

딕셔너리 자료형
    리스트 자료형
        딕셔너리 자료형
            리스트 자료형
                리스트 자료형
'''


print(d3['k1'][0]['nest_key'][1][0])

###############
## Problem 4 ##
###############

# Use a set to find the unique values of the list below:
mylist = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
# set 자료형 특징 생각
# 리스트 자료형 > set 자료형 형변환 진행
print(set(mylist))


###############
## Problem 5 ##
###############

# You are given two variables:
age = 4
name = "Sammy"

# Use print formatting to print the following string:
"Hello my dog's name is Sammy and he is 4 years old"


'''
# 문자형 포매팅 복기
    1. % 포맷코드 이용
    2. format메서드 이용
    3. f-string 이용
'''


print("Hello my dog's name is %s and he is %d years old" % (name, age))

print("Hello my dog's name is {} and he is {} years old".format(name, age))

print(f"Hello my dog's name is {name} and he is {age} years old")
