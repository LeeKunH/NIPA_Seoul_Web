from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def main_page():
    # Pass in a user name
    # We insert it to the html with jinja2 templates!
    return render_template('main2_home.html')


@app.route('/signnp_form')
def signnp_form():
    return render_template('signup.html')


# 가입페이지에서 버튼을 누르면 감사 페이지로 넘어간다.
# 따라서 thank_you 함수에서는 url주소에 있는 변수를 해석이 가능해야 함
@app.route('/thank_you')
def thank_you():
    first_name = request.args.get('성')
    last_name = request.args.get('이름')

    return render_template('thankyou.html', 성=first_name, 이름=last_name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
