# import requests
# import xmltodict

# url = "http://openapi.d2b.go.kr/openapi/service/PrcurePlanInfoService/getDmstcPrcurePlanList?orderPrearngeMtBegin=201410&orderPrearngeMtEnd=201411&ServiceKey=7dee4cd07b8fb02a4b40365d6a07099916c46531a9c8951d70a943822add2628&resultType=json"

# params = {
#     "ServiceKey": "7dee4cd07b8fb02a4b40365d6a07099916c46531a9c8951d70a943822add2628",
#     "orderPrearngeMtBegin": "201401",
#     "orderPrearngeMtEnd": "201412"
# }

# res = requests.get(url, params=params)

# data = xmltodict.parse(res.text)

# items = data["response"]["body"]["items"]["item"]

# print(items[0].keys())

# import requests
# import xmltodict

# url = "http://openapi.d2b.go.kr/openapi/service/PrcurePlanInfoService/getDmstcPrcurePlanList?orderPrearngeMtBegin=201410&orderPrearngeMtEnd=201411&ServiceKey=7dee4cd07b8fb02a4b40365d6a07099916c46531a9c8951d70a943822add2628&resultType=json"

# params = {
#     "ServiceKey": "7dee4cd07b8fb02a4b40365d6a07099916c46531a9c8951d70a943822add2628",
#     "orderPrearngeMtBegin": "201401",
#     "orderPrearngeMtEnd": "201412"
# }

# res = requests.get(url, params=params)

# data = xmltodict.parse(res.text)

# items = data["response"]["body"]["items"]["item"]

# print("데이터 개수:", len(items))
# print(data["response"]["body"]["totalCount"])

import requests
import xmltodict
import pandas as pd
import os

API_KEY = "여기에본인API키"

url = "http://openapi.d2b.go.kr/openapi/service/PrcurePlanInfoService/getDmstcPrcurePlanList?orderPrearngeMtBegin=201410&orderPrearngeMtEnd=201411&ServiceKey=7dee4cd07b8fb02a4b40365d6a07099916c46531a9c8951d70a943822add2628&resultType=json"

all_items = []
page = 1
num_rows = 100

while True:
    params = {
        "ServiceKey": "7dee4cd07b8fb02a4b40365d6a07099916c46531a9c8951d70a943822add2628",
        "orderPrearngeMtBegin": "201401",
        "orderPrearngeMtEnd": "201412",
        "pageNo": page,
        "numOfRows": num_rows
    }

    res = requests.get(url, params=params)
    data = xmltodict.parse(res.text)

    body = data["response"]["body"]
    total_count = int(body["totalCount"])

    items = body.get("items", {}).get("item", [])

    if isinstance(items, dict):
        items = [items]

    if not items:
        break

    all_items.extend(items)

    print(f"{page} 페이지 완료 / 현재 {len(all_items)}개 / 전체 {total_count}개")

    if len(all_items) >= total_count:
        break

    page += 1

# pandas DataFrame 생성
df = pd.DataFrame(all_items)

print("전체 데이터 개수:", df.shape)
print(df.head())

# CSV 저장
print("현재 폴더:", os.getcwd())
df.to_csv("procurement_data.csv", index=False, encoding="utf-8-sig")
print("CSV 저장 완료")