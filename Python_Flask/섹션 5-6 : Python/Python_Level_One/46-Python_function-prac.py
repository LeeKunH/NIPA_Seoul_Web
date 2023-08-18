
# 함수에 입력한 인수가 모음인지 확인하는 함수를 정의
def function_maker(mystring):
    for letter in mystring:
        for vowel in 'aeiou':
            print(f"입력한 문자 : {letter} 모음 확인 여부 : {letter == vowel}")


# 각 문자를 5번씩 확인함. 수정이 필요
function_maker('apple')

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")

# 일치하는 항목이 있는 경우에만 출력하도록 수정


def function_maker2(mystring):
    for vower in 'aeiou':
        if vower in mystring:
            print(f"입력한 문자 {mystring}안에는 모음 {vower} 존재")


function_maker2('apple')

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")

# 영상풀이


def function_maker(mystring):
    for letter in mystring:
        for vower in 'aeiou':
            if letter == vower:
                print(f"입력한 문자 : {mystring} 모음 : 모음 확인 여부 : {letter}")


function_maker('sammy')

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")

# 영상 문제 의도를 제대로 파악하지 못했음. 이렇게 출력되야 했음
# 코드 기록


def function_maker(mystring):
    '''
    어떤 기능이 담긴 함수?
    인수에 모음이 있는지 없는지 확인하고
    인수가 들어있는 부분을 X표시로 대체.
    '''

    output = list(mystring)  # 인수를 리스트 변환
    # enumerate내장함수 이용 인수의 인덱스와 각각 인수 접근
    for index, letter in enumerate(mystring):
        for vower in 'aeiou':  # 모음 1개씩 비교
            if letter.lower() == vower:
                output[index] = 'X'

    return output


answer = function_maker('Sammy')
print(answer)
answer = ''.join(answer)
print(answer)
