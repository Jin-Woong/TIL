from flask import Flask, request
# from telegram import send_message
import pprint
import requests
from decouple import config

app = Flask(__name__)

token = config('TOKEN')
api_url = f'https://api.telegram.org/bot{token}'


#   127.0.0.1/
@app.route("/")
def hello():
    return "Hello World!"


#   127.0.0.1/telegram
# @app.route('/telegram')
# def telegram2():
#     send_message('함수 전달 완료')
#     return '전송완료'


@app.route(f'/{token}', methods=['POST'])
def telegram():
    pprint.pprint(request.get_json())
    message = request.get_json().get('message')
    if message is not None:
        chat_id = message.get('from').get('id')  # 명시적으로 나타내기위해 get 사용 추천
        text = message.get('text')
        
        if text == '점심메뉴':
            # 점심메뉴를 확인하는 메뉴
            text = '점심메뉴'
        
        elif text == '로또':
            # 로또를 확인하는 코드
            text = '특정 로또번호'

        requests.get(api_url + f'/sendMessage?chat_id={chat_id}&text={text}')
    return '', 200


# app.py 파일이 `python app.py`로시작 되었을 때 작용
if __name__ == '__main__':
    app.run(debug=True)  # 서버가 켜져 있는 동안 수정이 발생하면 자동으로 재시작
