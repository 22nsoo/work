from flask import Flask, render_template,request

app = Flask(__name__);

@app.route("/")
def index():
    return render_template("index.html");

@app.route("/condition")
def condition():
    score = 85;
    return render_template("condition.html",score=score);

@app.route("/loop")
def loop():
    users = ["손오공", "사오정", "저팔계"];
    return render_template("loop.html", users=users);

@app.route("/filter")
def filter():
    message = "hello flask jinja2"
    price = 12345
    return render_template("filter.html", message=message, price=price);

@app.route("/get_form")
def get_form():
    return render_template("get_form.html");

@app.route("/get_result")                                               #method 안쓰면 GET 방식
def get_result():
    name = request.args.get("username");                                #get 방식일 땐 args로 받기
    age = request.args.get("age");                                      #숫자도 '23' 문자 타입으로만 받는다
    age = age + '살'
    return render_template("get_result.html", name=name, age=age);

@app.route("/post_form")
def post_form():
    return render_template("post_form.html");

@app.route("/post_result", methods=['POST'])
def post_result():
    name = request.form.get("username");
    email = request.form.get("email");
    return render_template("post_result.html", name=name, email=email);

if __name__ == "__main__":
    app.run(debug=True)
