from flask import Flask, render_template
app = Flask(__name__)


# # 애플리케이션 기본 라우팅

# @app.route('/')
# def index():
#     return render_template('basic.html')

# 플라스크에 들어있는 jinja 템플릿 엔진으로 인해 html코드 파일 위에서 파이썬 변수가 사용/렌더링 가능해짐
@app.route('/')
def index():
    # Pass in a user name
    # We insert it to the html with jinja2 templates!
    return render_template('main_home.html')


'''
    <h1> html파일 위에서 파이썬 변수 동작하는지 확인 시 URL창에 /user/name 입력!!! </h1> \n
    or <h1> html파일 위에서 파이썬 리스트-딕셔너리가 동작하는지 확인 시 URL창에/users/name 입력!!! </h1> \n
    or <h1> html파일 위에서 파이썬 제어문이 동작하는지 확인 시 URL창에 /control_flow/name 입력!!! </h1> \n
    or <h1> html파일 위에서 파이썬 제어문 사용 예시 확인 시 URL창에 /control_flow2/name 입력!!! </h1> \n
    <h1> 파이썬 플라스크 extend 상속, filter 기능 확인 시
    파이썬 제어문이 동작하는지 확인 시 URL창에 /extend_filer/name 입력!!! </h1>
    '''


@app.route('/imformation')
def info():
    return


@app.route('/users/<name>')
def users_name(name):
    letters = list(name)
    pup_dict = {'pup_name': name}

    return render_template('basic_jinja.html', html_name=name, mylist=letters, mydict=pup_dict)


@app.route('/control_flow/<name>')
def control_flow(name):
    # 파이썬 반목분
    mylist = [1, 2, 3, 4, 5]

    # 파이썬 조건문
    puppies = ['Fluffy', 'Rufus', 'Spike']
    return render_template('basic_control_flow.html', mylist=mylist, puppies=puppies)


@app.route('/control_flow2/<name>')
def control_flow2(name):
    # html파일 위에서 파이썬 제어문 사용 예시
    # 로그인 확인 유무
    '''
    로그인 기능을 구현한 코드가 있다고 가정
    '''
    user_loggeed_in = True
    return render_template('basic_control_flow.html', user_loggeed_in=user_loggeed_in)


@app.route('/extend_filer/<name>')
def extend_filer(name):
    return render_template('side_page.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
