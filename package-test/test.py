import main_package

'''
ㅡ
main_package 패키지 접근 > submodule_a 패키지 접근 > (some_module 모듈 접근) > submodule_function_a 함수 접근 호출!
ㅡ
main_package 패키지 접근 > submodule_b 모듈 접근 > submodule_function_b 함수 접근 호출!
'''

main_package.submodule_a.submodule_function_a()  # 출력: This is submodule A function.
main_package.submodule_b.submodule_function_b()  # 출력: This is submodule B function.
