from flask import Flask, render_template, request
import random
import requests

app = Flask(__name__)  # app 을 초기화 시켜주는 과정


# decorator 를 통해 어떤 route 로 들어올 때 동작하는지 설정
@app.route("/")
def hello():
    return "Hello World!"


@app.route('/hello')
def hello_new():
    return "Hello new World"


@app.route('/greeting/<string:name>')
def greeting(name):
    return f'반갑습니다! {name}님'


@app.route('/cube/<int:num>')
def cube(num):
    result = num ** 3
    return str(result)


@app.route('/lunch/<int:person>')
def lunch(person):
    menu = ['짜장면', '짬뽕', '탕수육', '볶음밥']
    result = random.sample(menu, person)
    return f'{result} 주문할게요'


@app.route('/html')
def html():
    return '''
    <h1>Happy Hacking!</h1>
    <p>즐겁게 코딩합시다 :)</p>
    '''


@app.route('/html_file')
def html_file():
    return render_template('html_file.html')


@app.route('/hi/<string:name>')
def hi(name):
    return render_template('hi.html', name=name)


@app.route('/cube_new/<int:number>')
def cube_new(number):
    result = number ** 3
    return render_template('cube_new.html', number=number, result=result)


@app.route('/naver')
def naver():
    return render_template('naver.html')


@app.route('/send')
def send():
    return render_template('send.html')


@app.route('/receive')
def receive():
    username = request.args.get('username')
    message = request.args.get('message')
    return render_template('receive.html', username=username, message=message)


# 사용자의 username 과 password 를 input 으로 받는다
# form action 을 통해 login_check 로 redirect 한다.
@app.route('/login')
def login():
    return render_template('login.html')


# 사용자의 입력이 admin /admin123 이 맞는지 확인한다.
# 맞으면 '환영합니다.' 아니면 '관리자가 아닙니다.'라고 출력한다.
@app.route('/login_check')
def login_check():
    username = request.args.get('username')
    password = request.args.get('password')
    if username == 'admin' and password == 'admin123':
        message = '환영합니다.'
    else:
        message = '관리자가 아닙니다.'
    return render_template('login_check.html', message=message)


# 사용자의 lotto 인풋을 받는다.
# lotto_result 로 보낸다.
@app.route('/lotto_check')
def lotto_check():
    return render_template('lotto_check.html')


@app.route('/lotto_result')
def lotto_result():
    lotto_round = request.args.get('lotto_round')
    numbers = [int(num) for num in lotto_round.split()]
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=860'
    response = requests.get(url)
    json = response.json()
    num_list = [json[f'drwtNo{i}'] for i in range(1, 7)]
    addnum = [json['bnusNo']]
    result = list(set(numbers) & set(num_list))
    bonus = list(set(numbers) & set(addnum))
    result.sort()
    if len(numbers) == 6:
        if len(result) == 6:
            message = '1등 입니다'
        elif len(result) == 5 and len(bonus) == 1:
            result.append(bonus[0])
            message = '2등 입니다'
        elif len(result) == 5:
            message = '3등 입니다'
        elif len(result) == 4:
            message = '4등 입니다'
        elif len(result) == 3:
            message = '5등 입니다'
        else:
            message = '꽝 입니다'
    else:
        message = '숫자가 6개가 아닙니다.'

    return render_template('lotto_result.html',
                           numbers=numbers, num_list=num_list, addnum=addnum, result=result, message=message)


# app.py 파일이 `python app.py`로시작 되었을 때 작용
if __name__ == '__main__':
    app.run(debug=True)  # 서버가 켜져 있는 동안 수정이 발생하면 자동으로 재시작
