import requests


"""
获取历史汇率

测试链接:
    https://api.investing.com/api/financialdata/historical/9618?start-date=2022-10-01&end-date=2022-10-14&time-frame=Daily&add-missing-rows=false
    -- usd  --> vnd
    https://api.investing.com/api/financialdata/historical/2214?start-date=2022-10-01&end-date=2022-10-14&time-frame=Daily&add-missing-rows=false
    -- usd --> hkd
    https://api.investing.com/api/financialdata/historical/155?start-date=2022-10-01&end-date=2022-10-14&time-frame=Daily&add-missing-rows=false
"""


url = "https://api.investing.com/api/financialdata/historical/155?start-date=2022-10-01&end-date=2022-10-14&time-frame=Daily&add-missing-rows=false"

headers = {
    "authority": "api.investing.com",
    "path": "/api/financialdata/historical/155?start-date=2022-10-01&end-date=2022-10-14&time-frame=Daily&add-missing-rows=false",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "sec-ch-ua-platform": "Windows"
}

def parse_json(url, params={}):
    """
        解析url,得到字典
    """
    response = requests.get(url=url, headers=headers, params=params)
    return response.json()

content = parse_json(url)
print(content)
