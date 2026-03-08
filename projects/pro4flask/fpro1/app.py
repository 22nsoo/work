#pip install flask
from flask import Flask             ##웹서버(Application Server) 생성에 필요

app = Flask(__name__);              #Flask 객체 생성, __name__: 현재 모듈의 이름                                        
@app.route("/")                     #URL 매핑.(라우팅) 클라이언트 요청이 '/'(port번호 뒤에 아무것도 안씀)일때 아래 함수 수행        

def abc():                          #클라이언트 요청을 처리하는 함수
    return "<h1>안녕하세요</h1> 반가워요"; 

@app.route("/about")
def about():
    return "플라스크를 소개하자면 만세~~~~";

@app.route("/user/<name>")          #URL에 변수를 담아 요청
def user(name):
    return f'내 친구 {name}';

if __name__ =='__main__':
    #학습용
    app.run();
    
