from flask import Flask, request
app = Flask(__name__)


# 애플리케이션 기본 라우팅
@app.route('/')
def index():
    return '''

    <div style="background-color: lightgray; margin: 10px; padding: 10px;" >
        <h1>이번 강의에서는 Flask 애플리케이션을 만든다!!!</h1>
        <img src="0c4219dd-4a84-4ceb-9169-6912c706a278.jfif" alt="플라스크 이미지">

        <h3> "Flask 프레임워크를 import해 가져와 사용하겠다"는 준비 작업이고, "Flask 애플리케이션을 만든다"는 실제 웹 애플리케이션을 구축하는 과정을 의미한다.</h3>

        <h3> route('/')는 메인 페이지에 방문에 대한 요청이 들어오면!! ~ 함수를 응답하겠다. 느낌
        </h3>
    </div>


    <div style="background-color: #ADD8E6; margin: 10px; padding: 10px;">
        <h1>섹션 7: Flask 기초 라우팅 연습 문제 풀이</h1>

        <h3>이름 자동 변환 웹 사이트에 오신 것을 환영합니다!!!</h3>

        <small>(이름의 마지막 글자가 "휘"로 끝나면 "희"로 변환, 아니라면 이름의 첫 글자가 "김"씨로 변환됨)</small>
<p>아래 입력폼에 이름을 입력해주세요.</p>

        <form action='/user/' method='get'>
            <input type='text' name='name' placeholder='웹 페이지 출력하고 싶은 이름입력' style='width: 250px;'>
            <br>
            <br>
            <input type='submit' value='사용자가 입력한 데이터를 라우팅 함수로 보내는 버튼' >
        </form>
    </div>

'''


@app.route('/imformation')
def info():
    return '''

  <h3> route('/')는 메인 페이지에 방문에 대한 요청이 들어오면!! ~ 함수를 응답하겠다. 느낌
    </h3>
  <h3> route('/information')는 메인 페이지에 연결된 information페이지에 대한 요청이 들어오면!! ~ 함수를 응답하겠다. 느낌
    </h3>

'''

# 플라스크 동적 라우팅
# 1번 방법으로 라우팅 함수를 작성하면 input으로 입력한 데이터를 변수로써 인식하지 못하고 문자열로 인식해서 화면에 제대로 출력되지 않음. 따라서 2번 방식으로 작성해서 쿼리 문자열에서 데이터를 뽑아와야함

# 1번
# @app.route('/user/<name>')
# def kor_user(name):
#     # Page for an individual user.
#     return f'<h1>{name}의 페이지는 동적으로 반응하고 있다!!!<h1>'

# 2번
@app.route('/user/')
def kor_user():
    name = request.args.get('name')

    if name[-1] == "휘":
        new_name = list(name)
        new_name[-1] = "희"
        name = ''.join(new_name)
    else:
        new_name = list(name)
        new_name[0] = "김"
        name = ''.join(new_name)

    return f'<h1>{name}의 페이지는 동적으로 반응하고 있다!!!<h1>'


# 기본 Flask앱 실행
if __name__ == '__main__':
    app.run(debug=True)