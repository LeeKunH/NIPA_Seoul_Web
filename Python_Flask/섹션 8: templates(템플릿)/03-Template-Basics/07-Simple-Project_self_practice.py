from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def main_page():
    # 메인 페이지 호출되면 함수 반환응답
    return render_template('main3_home.html')


@app.route('/check_conditions')
def check_conditions():

    lower_letter = False
    upper_letter = False
    num_end = False
    username = request.args.get('username')

    # 조건 로직 작성
    lower_letter = any(c.islower() for c in username)
    upper_letter = any(c.isupper() for c in username)
    # so1)1 num_end
    num_end = username[-1].isdigit()

    # # sol)2 num_end
    # if (int(username[-1])):
    #     # 참이라면 숫자를 입력한 것
    #     num_end = True
    # else:
    #     num_end = False

    # 3개 조건이 모두 참이라면 report = T
    # 1개라도 아니라면 report = F
    check_conditions = lower_letter and upper_letter and num_end

    # 3개 조건 모두 참일때 확인하기 위한 check_conditions 변수 할당.
    # 3개 조건 모두 참이 아닐 땐 각각 참<>거짓 여부 확인을 위한 lower_letter, upper_letter, num_end 변수 할당.
    return render_template('result_screen.html', check_conditions=check_conditions, lower_letter=lower_letter, upper_letter=upper_letter, num_end=num_end)


if __name__ == '__main__':
    app.run(debug=True)
