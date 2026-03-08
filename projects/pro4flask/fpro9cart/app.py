from flask import Flask, render_template, redirect, url_for, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "abcdef123456"
app.permanent_session_lifetime = timedelta(minutes=5)

products = [
    {"id": 1, "name": "노트북", "price": 3500000},
    {"id": 2, "name": "키보드", "price": 50000},
    {"id": 3, "name": "마우스", "price": 35000},
    {"id": 4, "name": "모니터", "price": 150000},
]

@app.route("/")
def product_list():
    return render_template("products.html", products=products)

@app.route("/cart")
def show_cart():
    cart = session.get("cart", {})
    total = sum(info["price"] * info["qty"] for info in cart.values())
    return render_template("cart.html", cart=cart, total=total)

@app.route("/add/<int:product_id>")
def add_to_cart(product_id):
    cart = session.get("cart", {})
    product = next((p for p in products if p["id"] == product_id), None)

    if product is None:
        return "상품 정보를 찾을 수 없어요", 404

    item_name = product["name"]

    if item_name in cart:
        cart[item_name]["qty"] += 1
    else:
        cart[item_name] = {"price": product["price"], "qty": 1}

    session["cart"] = cart
    session.permanent = True
    return redirect(url_for("show_cart"))

# 장바구니 부분 삭제

@app.route("/remove/<item_name>")
def remove_to_cart(item_name):
    cart = session.get("cart", {})
    if item_name in cart:
        del cart[item_name]
        session["cart"] = cart                  # 변수 cart를 세션 "cart"키에 값으로 저장
        session.permanent = True                # 5분 만료 적용
    return redirect(url_for("show_cart"))       # redirect: 서버에 있는데 클라이언트를 통해서 부를 때 사용 원래는 클라이언트가 요청을 해야 부를 수 있지만
                                                # redirect를 쓰면 서버에서 라우팅 된것을 부를 수 있다.

# 몽땅 지우기

@app.route("/clear")
def clear_cart():
    session.pop("cart", None)                   #세션에 여러개의 키 중에서 "cart"라는 키를 삭제
    return redirect(url_for("show_cart"))

if __name__ == "__main__":
    app.run(debug=True)