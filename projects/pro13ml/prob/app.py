from flask import Flask, render_template, request, jsonify
import pymysql
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

app = Flask(__name__)

db_config = {
    'host':'127.0.0.1',
    'user':'root', 
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8mb4'
}

def get_connection() :
    return pymysql.connect(**db_config)

# 전역 변수
model = None
r2 = None
coef_ = None
intercept_ = None
job_avg = None

# 서버 시작 시 모델 생성
def load_model():
    global model, r2, coef_, intercept_, job_avg

    conn = get_connection()

    sql = """
        SELECT
            TIMESTAMPDIFF(YEAR, jikwonibsail, CURDATE()) AS years,
            jikwonpay AS pay,
            jikwonjik AS jik
        FROM jikwon
        WHERE jikwonibsail IS NOT NULL
          AND jikwonpay IS NOT NULL
    """

    df = pd.read_sql(sql, conn)
    conn.close()

    print(df.head())
    print(df.dtypes)

    # 숫자형으로 강제 변환
    df['years'] = pd.to_numeric(df['years'], errors='coerce')
    df['pay'] = pd.to_numeric(df['pay'], errors='coerce')

    # 숫자 변환 실패한 행 제거
    df = df.dropna(subset=['years', 'pay'])

    # 독립변수 X, 종속변수 y
    X = df[['years']]
    y = df['pay']

    lr = LinearRegression()
    lr.fit(X, y)

    y_pred = lr.predict(X)
    score = r2_score(y, y_pred)

    job_avg_df = (
        df.groupby('jik', as_index=False)['pay']
        .mean()
        .sort_values('jik')
    )
    job_avg_df['pay'] = job_avg_df['pay'].round(0).astype(int)

    model = lr
    r2 = score
    coef_ = lr.coef_[0]
    intercept_ = lr.intercept_
    job_avg = job_avg_df.to_dict(orient='records')


@app.route('/')
def index():
    return render_template(
        'index.html',
        predicted_pay=None,
        years=None,
        r2=r2,
        coef_=coef_,
        intercept_=intercept_,
        job_avg=job_avg
    )


@app.route('/predict', methods=['POST'])
def predict():
    years = request.form.get('years')

    try:
        years = float(years)
    except:
        return jsonify({
            'success': False,
            'message': '근무년수를 숫자로 입력하세요.'
        })

    pred = model.predict([[years]])[0]

    return jsonify({
        'success': True,
        'years': years,
        'predicted_pay': round(pred, 2),
        'r2': round(r2 * 100, 2),
        'coef': round(coef_, 4),
        'intercept': round(intercept_, 4)
    })


if __name__ == '__main__':
    load_model()
    app.run(debug=True)